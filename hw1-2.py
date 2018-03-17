# Homework 1 - Problem 2
# George Choumos

import snap as snap
import random
import time

# Default values for vertices and edges
n_ver_default = 50
n_edg_default = 10

print """
--------------
| First part |
--------------
Sample execution getting input from the user:
"""

###############################################
## Part 1 - Step 1 - Get and sanitize input! ##
###############################################

# Get the input from the user. If he inputs nothing or something invalid, the value will default to the default.
print "Please provide number of vertices - If no value or any 'funny' value given, it will default to %d: " % n_ver_default
try:
  n_ver = int(raw_input())
except ValueError:
  print("Using default...\n")
  n_ver = n_ver_default

# Let's also get the degree parameter for the vertice generation as an input
print "Please provide the vertice parameter. It should be in the range [5-20]"
print "If no value or any 'funny' value given, it will default to %d: " % n_edg_default

try:
  n_edg = int(raw_input())
except ValueError:
  print("Using default...\n")
  n_edg = n_edg_default

if n_edg < 5 or n_edg > 20:
  print "That was out of the specified range [5-20]. The default value will be used instead.\n"
  n_edg = n_edg_default



######################################
## Part 1 - Step 2 - Generate graph ##
######################################
# Now let's generate the graph using the Barabasi-Albert model.
Rnd = snap.TRnd()
graph = snap.GenPrefAttach(n_ver, n_edg, Rnd)


#####################################################################
## Part 1 - Step 3 - Calculate max outdegree and the relevant node ##
#####################################################################
# Note:
# It is highly likely that there will exist many nodes that share the max outdegree.
# We could either show them all or just pick one of them and show it.
# Actually, we will just do the latter.
max_outdeg = 0
max_nodeid = 0

for x in graph.Nodes():
  if x.GetOutDeg() > max_outdeg:
    max_outdeg = x.GetOutDeg()
    max_nodeid = x.GetId()
print "Maximum out degree is %d. Node id: %d" % (max_outdeg, max_nodeid)


####################################################################
## Part 1 - Step 4 - Calculate max PageRank and the relevant node ##
####################################################################
# Now we have to print out the id of the node with the highest PageRank  as well as the PageRank value.
# Like previously, it is possible that there may exist many nodes with the same pagerank
# value - although this is really rare. We will just keep the first encounter to display.
max_pagerank = -1.0
max_pagerank_id = 0

pagerank = snap.TIntFltH()
snap.GetPageRank(graph, pagerank)

for x in pagerank:
  if pagerank[x] > max_pagerank:
    max_pagerank = pagerank[x]
    max_pagerank_id = x
print "Maximum PageRank is %f. Node id: %d" % (max_pagerank, max_pagerank_id)


##################################################################
## Part 1 - Step 5 - GirvanNewman single execution time measure ##
##################################################################
# Measure the time needed for the execution of the GirvanNewman community detection algorithm
# based on betweenness centrality
start_time = time.time()

community_v = snap.TCnComV()
modularity = snap.CommunityGirvanNewman(graph, community_v)
#for x in community_v:
#  print "Community: "
#  for  y in x:
#    print y
#print "The modularity of the network is %f" % modularity
print "GirvanNewman - Execution time required: %f seconds" % (time.time() - start_time)

# Clear community vector
community_v = None


##########################################################################
## Part 1 - Step 6 - Clauset-Newman-Moore single execution time measure ##
##########################################################################
# Measure the time needed for the execution of the Clauset-Newman-Moore community detection method.
start_time = time.time()

community_v = snap.TCnComV()
modularity = snap.CommunityCNM(graph, community_v)
#for x in community_v:
#  print "Community: "
#  for y in x:
#    print y
#print "The modularity of the network is %f" % modularity
print "ClausetNewmanMoore - Execution time required: %f seconds" % (time.time() - start_time)



############
## Part 2 ##
############
print """
---------------
| Second part |
---------------
Repeated execution with increasing size of graph:


"""

# I'll start with 50 nodes and then in each iteration I'll be adding 1/10 of the previous nodes.
# So it'll be 50 --> 55 --> 60 --> 66 --> 72 --> 79 --> 86 --> 94 --> ... and so on
# The edge parameter will be 15
n_ver = 50
n_edg = 15

# Initialize general time - :p
# This will measure the whole execution.
start_time = time.time()

# And this is a helper for the consecutive executions
previous_time = start_time

# Iteration number
i = 1

# While 
while time.time() - start_time < 600:
  try:
    Rnd = snap.TRnd()
    graph = snap.GenPrefAttach(n_ver, n_edg, Rnd) 

    print "%d. Nodes: %d - Starting execution..." % (i,n_ver)

    # Execution of GirvanNewman community detection algorithm based on betweenness centrality
    community_v = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(graph, community_v)

    # Mini-cleanup for psychological reasons
    community_v = None

    # Execution of the Clauset-Newman-Moore community detection method.
    community_v = snap.TCnComV()
    modularity = snap.CommunityCNM(graph, community_v)

    # Print the results for the iteration
    print "Complete! Execution time required for both algorithms: %d seconds\n" % (time.time() - previous_time)

    # Clean up after ourselves
    graph = None
    community_v = None

    # Increment the number of vertices and the iteration
    n_ver += int(n_ver/10)
    i += 1

    # Set the new previous time appropriately
    previous_time = time.time()

  except MemoryError:
    print "\n\nLOL!! Memory Error!"
    break
else:
  # 10 minutes have passed!
  print "\n\nTIME OUT! 10 minutes have passed!"

print """

--------------------
| End of execution |
--------------------
"""

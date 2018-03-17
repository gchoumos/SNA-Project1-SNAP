# Homework 1 - Problem 1
# George Choumos

import snap as snap
import unittest

# Some of the things we consider for this exercise
# - The graph is going to be undirected. This means that the outdegree == indegree

# Checks if all vertices even
def has_all_vertices_even(graph):
  for x in graph.Nodes():
    if x.GetOutDeg() % 2 == 1:
	  return False

  # None odd found, so all even
  return True


# Returns odd degree vertices. If none exist, it will return the empty set.
def get_odd_vertices(graph):
  odd_vertices = set()
  for x in graph.Nodes():
    if x.GetOutDeg() % 2 == 1:
	  odd_vertices.add(x.GetId())

  return odd_vertices


# Checks if graph is connected
def is_connected(graph):
  # Just use the snap library to do that as the exercise points out.
  return snap.IsConnected(graph)


# If an euler path indeed exists, it will return the 2 vertices (start and end)
# If not it will return an empty set (regardless of how many odd-degree vertices exist).
def has_euler_path(graph):
  # It must:
  # ~ be connected
  # ~ have exactly 2 vertices with odd degree
  # ~ those 2 vertices will form the beginning and end of the path
  vertices = set()

  # Check if not connected
  if not is_connected(graph):
    return False, set()

  # Get the odd degree vertices
  vertices = get_odd_vertices(graph)

  if len(vertices) == 2:
    return True, vertices
  else:
    return False, set()


def has_euler_circuit(graph):
  # It must:
  # ~ be connected
  # ~ all vertices must have even degree

  # Check if not connected
  if not is_connected(graph):
    return False

  # Check if all vertices have even degree
  if has_all_vertices_even(graph):
    return True
  else:
    return False

class TestEulerMethods(unittest.TestCase):

  def test_has_euler_path_but_not_circuit(self):

	# Create a sample graph for the first case. It is undirected, like all of them are.
	graph1 = snap.TUNGraph.New()
	# Add the nodes
	graph1.AddNode(1)
	graph1.AddNode(2)
	graph1.AddNode(3)
	graph1.AddNode(4)
	graph1.AddNode(5)
	graph1.AddNode(6)
	# Add the edges
	graph1.AddEdge(1,2)
	graph1.AddEdge(2,3)
	graph1.AddEdge(2,4)
	graph1.AddEdge(2,6)
	graph1.AddEdge(3,4)
	graph1.AddEdge(3,5)
	graph1.AddEdge(3,6)
	graph1.AddEdge(4,5)
	graph1.AddEdge(4,6)

	result, vertices = has_euler_path(graph1)
	self.assertTrue(result)
	self.assertEqual(len(vertices), 2)

  def test_does_not_have_euler_path(self):

    # This sample graph has 4 nodes with odd degree
    graph2 = snap.TUNGraph.New()
    # Add the nodes
    graph2.AddNode(1)
    graph2.AddNode(2)
    graph2.AddNode(3)
    graph2.AddNode(4)
    graph2.AddNode(5)
    graph2.AddNode(6)
    # Add the edges
    graph2.AddEdge(1,2)
    graph2.AddEdge(2,3)
    graph2.AddEdge(2,6)
    graph2.AddEdge(3,4)
    graph2.AddEdge(3,5)
    graph2.AddEdge(4,5)

    result, vertices = has_euler_path(graph2)
    self.assertFalse(result)
    self.assertEqual(len(vertices), 0)

  def test_has_euler_circuit(self):
    # We are going to create a graph which will be large enough. For this purpose we will
    # use a generator from the snap library. A circular graph seems to be the easiest pick
    # in order to satisfy the even degree limitation for all nodes.
    graph3 = snap.GenCircle(snap.PNGraph,1200,4,False)
    

    result = has_euler_circuit(graph3)
    self.assertTrue(result)
    self.assertTrue(graph3.GetNodes()>=1000)

  def test_does_not_have_euler_circuit(self):
    # Let's create a smaller version of the previous circle graph. Then remove one of its edges.
    # This means that there will be a vertice with odd degree which will "break" the Euler circuit.
    graph4 = snap.GenCircle(snap.PNGraph,16,4,False)
    graph4.DelEdge(1,2)
    
    result = has_euler_circuit(graph4)
    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

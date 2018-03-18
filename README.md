# README #

This repository holds the implementation of the first assignment for the **Social Network Analysis** half-course, which was part of the M.Sc. in Data Science of the Athens University of Economics and Business.

### Assignment Overview ###
The original assignment description itself is not available in this repo; however, here is an overview of what the code does.

I am using [Standford's **SNAP**](http://snap.stanford.edu/), which is a general purpose network analysis and graph mining library, in order to make some of the first steps with regards to SNAP familiarisation, graph creation, graph traversal, graph information extraction and community detection.

The pdf report on the repo is actually a walk through what has been implemented. You can download and see it in it's original form. However a markdown version of it follows at the end of this README file.


### How do I get set up? ###
Snap library is not native Python, so you will have to download and install it. You can find detailed instructions in [this link](http://snap.stanford.edu/snappy/index.html#download).

Have in mind that, at least at the time (March 2018) SNAP is only supported in Python 2.7 so consider this to be a prerequisite. This is the reason why some basic stuff like the print syntax in the code is of the python 2 format.

# Markdown Version of Assignment Report #

---------------

### Social Network Analysis - Homework 1
### George Choumos

This document just includes a really brief overview of how the 2 problems were solved. In fact, the scripts that are submitted are sufficiently commented and a read through them should be enough to give you a clear picture of the implementation details.

## Problem 1
The following functions have been implemented:


* **_`has_all_vertices_even`_**: Iterates through the graph nodes and checks if their degree is divisible by 2. If it finds one that has odd degree it returns False. Otherwise, if all nodes are checked and none is odd, it returns True.

* **_`get_odd_vertices`_**: Iterates through the graph nodes and adds the odd-degree ones in a set which it eventually returns. If none is found, then it just returns an empty set.

* **_`is_connected`_**: This is just a wrapper function that only calls SNAP's corresponding function and then returns the value that comes back.

* **_`has_euler_path`_**: Decides whether or not the given graph has an Euler path. At first, it checks if the graph is connected. Then it calls `get_odd_vertices` in order to get the nodes that have odd degree. If the graph is connected and the odd vertices are exactly 2, then the graph does have an Euler path. Otherwise, if any of the above checks fail, it does not.

* **_`has_euler_circuit`_**: Similar to the previous one, except for the fact that after the *connected* check, it also checks whether or not the nodes (all of them) have an even degree.

##### Test Cases Preparation
* **_`test_has_euler_path_but_not_circuit`_**: A graph is manually created, (not through a generator) with 6 nodes and 9 edges. 2 of the nodes have odd degree.

* **_`test_does_not_have_euler_path`_**: A graph is manually created again with 6 nodes and 6 edges. 4 of the nodes have odd degree.

* **_`test_has_euler_circuit`_**: Since we wanted a sufficiently large graph here, we used a generator. A circular graph seemed to be the easiest pick in order to satisfy the even-degree prerequisite for all nodes.

* **_`test_does_not_have_euler_circuit`_**: I created a smaller version of the previous graph (as I didn't have size limitations here) and then just deleted an edge.


## Problem 2
### *First part*
The script is implemented so that it gets the number of nodes and edges from the user upon execution. There exist default values as well, 50 for the number of nodes and 10 for the number of edges.

Input checks are provided so that if the user enters no value or something that is not a number or not in the acceptable range, the defaults are being used instead.

The graph in the first part is generated using SNAP's *`GenPrefAttach`* generator.

Max outdegree is calculated and printed along with the node id that holds it. In fact, as I mention in the comments, it is quite possible that the maximum outdegree is going to be shared by many nodes. We could either print all of the tied outdegree nodes or just keep and print one of them. I used the second approach as it seems sufficient for the purpose of this exercise.

Then, the *PageRank* max value is calculated in the same manner as with the outdegree. The probability of a tie in this case is quite smaller though.

The next step is to measure the time that is required for the **_Girvan-Newmann_** community detection algorithm. I am using the *time* module to achieve this. Right after, similar functionality is triggered in order to measure the time required for the **_Clauser-Newmann-Moore_** community detection algorithm. Printing the communities is commented out as I don't think it has much to offer and because of the fact that we are actually interested in the execution time.


### *Second Part*
We are starting with 50 nodes and 15 as the edge parameter. The edge parameter remains stable but the nodes are incremented. We actually add 10% of the nodes in each iteration. This means that for the first iterations the nodes will be 50, 55, 60, 66, 72, 79, 86 ... and so on.

There are 2 cases for execution termination. We either receive a memory error or we are at a time point which is more than 10 minutes from the moment that the script's execution started.

In each iteration, you will see output for the number of the nodes that are in the generated graph, as well as the number of the edges parameter. When the execution of the iteration ends, you will also see in the output how much time it took this iteration to finish.

I have added a handler for the *MemoryError* exception so that the script doesn't fail, but terminate graciously instead.



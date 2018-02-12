""".

https://www.coursera.org/learn/algorithmic-thinking-1/supplement/hw1o3/project-1-description

Graphs knoledge: https://storage.googleapis.com/codeskulptor-alg/pdf/GraphBasics.pdf

Project description: https://www.coursera.org/learn/algorithmic-thinking-1/supplement/hw1o3/project-1-description
Graph0: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph0.jpg
Graph1: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph1.jpg
Graph2: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph2.jpg
"""


EX_GRAPH0 = {0: {1, 2}, 1: {}, 2: {}}

print(EX_GRAPH0)
print(type(EX_GRAPH0[0]))

EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: {}}

print(EX_GRAPH1)

EX_GRAPH2 = {0: {1, 4, 5},
             1: {2, 6},
             2: {3, 7},
             3: {7},
             4: {1},
             5: {2},
             6: {},
             7: {3},
             8: {1, 2},
             9: {0, 3, 4, 5, 6, 7}}

print(EX_GRAPH2)


def make_complete_graph(num_nodes):
    """.
    Takes the number of nodes num_nodes and returns a dictionary corresponding
    to a complete directed graph with the specified number of nodes.
    A complete graph contains all possible edges subject to the restriction
    that self-loops are not allowed. The nodes of the graph should be
    numbered 0 to num_nodes - 1 when num_nodes is positive.
    Otherwise, the function returns a dictionary
    corresponding to the empty graph.
    """

    graph = {i: {k for k in range(num_nodes) if k != i} for i in range(num_nodes)}
    return graph


print(make_complete_graph(5))


def compute_in_degrees(digraph):
  """.
  Takes a directed graph  (represented as a dictionary) and computes the
  in-degrees for the nodes in the graph. The function should return a dictionary
  with the same set of keys (nodes) as  whose corresponding values are the number
  of edges whose head matches a particular node.
  """

  d = {}
  keys = digraph.keys()

  d = {key: 0 for key in keys}

  for key in keys:
      for el in digraph[key]:
          d[el] += 1

  return d

def in_degree_distribution(digraph):
	""".
	Takes a directed graph  (represented as a dictionary) and computes the unnormalized
	distribution of the in-degrees of the graph.
	The function should return a dictionary whose keys correspond to in-degrees of nodes in
	the graph. The value associated with each particular in-degree is the number of nodes
	with that in-degree. In-degrees with no corresponding nodes in the graph are not
	included in the dictionary.
	"""
	d_distr = {}
	d = compute_in_degrees(digraph)

	for (key,value) in d.items():
			d_distr[value] = d_distr.get(value,0) + 1

	return d_distr

print(compute_in_degrees(EX_GRAPH2))  # {0: 1, 1: 3, 2: 3, 3: 3, 4: 2, 5: 2, 6: 2, 7: 3, 8: 0, 9: 0}
print(in_degree_distribution(EX_GRAPH2))  # {1: 1, 2: 3, 3: 4}

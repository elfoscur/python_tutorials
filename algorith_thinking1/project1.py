""".
https://www.coursera.org/learn/algorithmic-thinking-1/supplement/hw1o3/project-1-description
Graphs knoledge: https://storage.googleapis.com/codeskulptor-alg/pdf/GraphBasics.pdf
Project description: https://www.coursera.org/learn/algorithmic-thinking-1/supplement/hw1o3/project-1-descriptionGraph0: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph0.jpgGraph1: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph1.jpgGraph2: http://storage.googleapis.com/codeskulptor-alg/alg_example_graph2.jpg"""
EX_GRAPH0 = {0: {1, 2}, 1: {}, 2: {}}
print(EX_GRAPH0)print(type(EX_GRAPH0[0]))
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: {}}
print(EX_GRAPH1)
EX_GRAPH2 = {0: {1, 4, 5},             1: {2, 6},             2: {3, 7},             3: {7},             4: {1},             5: {2},             6: {},             7: {3},             8: {1, 2},             9: {0, 3, 4, 5, 6, 7}}
print(EX_GRAPH2)
def make_complete_graph(num_nodes):    """.    Takes the number of nodes num_nodes and returns a dictionary corresponding    to a complete directed graph with the specified number of nodes.    A complete graph contains all possible edges subject to the restriction    that self-loops are not allowed. The nodes of the graph should be    numbered 0 to num_nodes - 1 when num_nodes is positive.    Otherwise, the function returns a dictionary    corresponding to the empty graph.    """
    graph = {i: {k for k in range(num_nodes) if k != i} for i in range(num_nodes)}    return graph
print(make_complete_graph(5))
def compute_in_degrees(digraph):    """.    Takes a directed graph  (represented as a dictionary) and computes the    in-degrees for the nodes in the graph. The function should return a dictionary    with the same set of keys (nodes) as  whose corresponding values are the number    of edges whose head matches a particular node.    """
    d = {}    keys = digraph.keys()    d = ({i:k for k in keys for i in digraph[k]})    return d
print(compute_in_degrees(EX_GRAPH1))
d = {}

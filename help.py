import random
from typing import List

import networkx


def _random_subset(seq: List[int], m: int, rnd):
    """ Return m unique elements from seq.
    Note: rng is a random.Random or numpy.random.RandomState instance.
    """
    targets = set()
    while len(targets) < m:
        x = rnd.choice(seq)
        targets.add(x)
    return targets


def barabasi_albert_graph(n: int, m: int, t: int, rnd) -> networkx.Graph:
    '''
    :param n: start amount of nodes in full graph
    :param m: amount of edges for new vertex
    :param t: amount of new nodes to add
    :param rnd: random generator
    :return: graph
    '''

    graph = networkx.complete_graph(n)
    if n < m:
        return

    # Target nodes, to which we will connect new created node
    targets = list(range(m))

    # list of nodes to choose new targets. Every node appears its "degree" times
    repeated_nodes = []
    for node in range(n):
        #   add every node to repeated_nodes (n - 1) times
        repeated_nodes.extend([node] * (n - 1))

    # source = name of new node
    source = n
    while source < n + t:
        # Add edges to m nodes from the source. If we need to add node 3 to nodes 0 and 1 ->
        # zip will return something like ((3, 0), (3, 1))
        graph.add_edges_from(zip([source] * m, targets))

        # Target nodes will have one connection more -> indegree will increase by 1 ->
        # we add it one more time to repeated_nodes
        repeated_nodes.extend(targets)
        # New node "source" now have m edges, so we add it m times to repeated_nodes
        repeated_nodes.extend([source] * m)
        # Now choose m unique nodes from the repeated_nodes. Probability depends on degree of node (number of edges)
        targets = _random_subset(repeated_nodes, m, rnd)
        source += 1
    return graph


n, m, t = 3, 2, 1
graph = barabasi_albert_graph(n, m, t, random)
print(graph.edges)

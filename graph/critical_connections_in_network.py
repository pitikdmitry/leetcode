'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections
forming a network where connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
'''
from collections import defaultdict
from typing import List


#   Tarjan's critical connection algorithm
class Solution:
    def dfs(self, prev_node, node, node_id_counter, graph, nodes_ids, low_link_values, visited, critical_connections):
        visited.add(node)

        #   assign id to node
        nodes_ids[node] = node_id_counter
        #   assign low-link value
        low_link_values[node] = node_id_counter
        node_id_counter += 1

        for child in graph[node]:
            #   prevent call to previous node (parent node)
            if child == prev_node:
                continue

            if child not in visited:
                self.dfs(node, child, node_id_counter, graph, nodes_ids, low_link_values, visited, critical_connections)
                #   connection is critical if child node can't find path to current node or smaller node
                if low_link_values[child] > nodes_ids[node]:
                    critical_connections.append([node, child])

            #   update lo-link value
            low_link_values[node] = min(low_link_values[node], low_link_values[child])

        return low_link_values[node]

    def convert_graph(self, connections):
        graph = defaultdict(list)
        for fr, to in connections:
            graph[fr].append(to)
            graph[to].append(fr)
        return graph

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.convert_graph(connections)

        visited, nodes_ids, low_link_values, critical_connections = set(), {}, {}, []

        #   we can start dfs from every node, because all graph is one connected component
        previous_node, start_node, node_id_counter = -1, 0, 0
        self.dfs(previous_node, start_node, node_id_counter, graph, nodes_ids, low_link_values, visited, critical_connections)

        return critical_connections


solution = Solution()
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(solution.criticalConnections(n, connections))

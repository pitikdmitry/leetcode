'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''
from typing import List, Dict
from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.children = []
        self.in_degree = 0


#   Topological order Kahn's algorithm
class Solution:
    def transform_graph(self, prerequisites: List[List[int]]) -> Dict[int, Node]:
        graph = defaultdict(Node)
        for pair in prerequisites:
            course = pair[0]
            prev_course = pair[1]

            graph[course].children.append(prev_course)
            graph[prev_course].in_degree += 1
        return graph

    #   add courses without dependencies to graph
    def add_single_nodes(self, num_courses: int, graph: Dict[int, Node]) -> Dict[int, Node]:
        course_num = 0
        while len(graph) < num_courses:
            if course_num not in graph:
                graph[course_num] = Node()
            course_num += 1

        return graph

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.transform_graph(prerequisites)
        graph = self.add_single_nodes(numCourses, graph)
        topological_order = []
        nodes_find = 0
        #   finding nodes with indegree=0, until we processed all graph
        while nodes_find < numCourses:
            found_node = False
            for node_val, node in graph.items():
                if node.in_degree == 0:
                    found_node = True
                    nodes_find += 1
                    topological_order.append(node_val)

                    #   instead of deleting node
                    node.in_degree = -1

                    #   decreasing indegree if children
                    for child_val in node.children:
                        child_node = graph[child_val]
                        child_node.in_degree -= 1

                    break

            #   if we can't find node with indegree = 0 -> there is a cycle -> no topological order
            if found_node is False:
                return []

        return list(reversed(topological_order))


solution = Solution()
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
num = 4
print(solution.findOrder(num, prerequisites))


from typing import List, Dict
from collections import defaultdict


#   instead of call_stack stack and visited set we will store this information in the object attributes
class Node:
    def __init__(self) -> None:
        self.children = []
        self.visited = False
        self.in_call_stack = False


#   Topological order approach via DFS
class Solution:
    #   transform graph from list of edges to adjacency list.
    #   But instead of List[int] we store info in Node with special variables
    def transform_graph(self, prerequisites: List[List[int]]) -> Dict[int, Node]:
        graph = defaultdict(Node)
        for pair in prerequisites:
            course = pair[0]
            prev_course = pair[1]
            graph[course].children.append(prev_course)
            #   initialization of course node
            graph[prev_course].visited = False
        return graph

    #   add courses without dependencies to graph
    def add_single_nodes(self, num_courses: int, graph: Dict[int, Node]) -> Dict[int, Node]:
        course_num = 0
        while len(graph) < num_courses:
            if course_num not in graph:
                graph[course_num] = Node()
            course_num += 1

        return graph

    def dfs(self, node_val: int, graph: Dict[int, Node], topological_order: List[int]) -> bool:
        node = graph.get(node_val)

        if node is None:
            return False

        if node.in_call_stack is True:
            return True

        if node.visited is True:
            return False

        node.in_call_stack = True
        node.visited = True

        children = node.children
        has_cycle = False
        if len(children) > 0:
            for child in children:
                has_cycle = self.dfs(child, graph, topological_order) or has_cycle

        node.in_call_stack = False
        topological_order.append(node_val)
        return has_cycle

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        graph = self.transform_graph(prerequisites)
        graph = self.add_single_nodes(numCourses, graph)
        topological_order = []
        has_cycle = False
        for start_node_val in graph.keys():
            has_cycle = self.dfs(start_node_val, graph, topological_order) or has_cycle

        if has_cycle is True or len(topological_order) != numCourses:
            return []

        return topological_order


solution = Solution()
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
num = 4
print(solution.findOrder(num, prerequisites))

solution = Solution()
prerequisites = [[1, 0]]
num = 3
print(solution.findOrder(num, prerequisites))

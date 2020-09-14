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
from typing import List


#   Topological order Kahn's algorithm
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, in_degree = {}, {}
        #   create all nodes
        for i in range(numCourses):
            graph[i] = []
            in_degree[i] = 0

        #   build graph and populate in_degree map
        for course, prev_course in prerequisites:
            graph[course].append(prev_course)
            in_degree[prev_course] += 1

        #   put nodes with zero indegree in queue
        q = []
        for node in in_degree.keys():
            if in_degree[node] == 0:
                q.append(node)

        topological_order = []
        #   keep track of found nodes, if it will be less than given amount of courses,
        #   than there is a cycle -> no topological order
        nodes_find = 0
        while len(q) > 0:
            node = q.pop()

            topological_order.append(node)
            nodes_find += 1

            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

        if nodes_find < numCourses:
            return []

        return list(reversed(topological_order))


solution = Solution()
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
num = 4
print(solution.findOrder(num, prerequisites))

'''There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C,
then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.'''
from typing import List, Dict


class Solution:
    def bfs(self, counter_friends: Dict[int, List[int]], key: int) -> None:
        q = []
        q.append(key)
        while len(q) > 0:
            key = q.pop(0)
            arr = counter_friends.get(key)

            if arr is None:
                continue
            del counter_friends[key]

            for arr_val in arr:
                q.append(arr_val)

    def findCircleNum(self, M: List[List[int]]) -> int:
        counter_friends = {}
        circles = 0

        #   convert to adjacency list
        for i in range(len(M)):
            for j in range(0, len(M[i])):
                if M[i][j] == 1:
                    if i not in counter_friends:
                        counter_friends[i] = []
                    counter_friends[i].append(j)

        while len(counter_friends) > 0:
            key = next(iter(counter_friends.keys()))
            self.bfs(counter_friends, key)
            circles += 1
        return circles


s = Solution()
M = [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 1]]
print(s.findCircleNum(M))


#   DFS solution without with adjacency matrix
class Solution:
    def dfs(self, friends: List[List[int]], i: int, visited: set) -> None:
        if i in visited:
            return
        visited.add(i)

        for j in range(len(friends[i])):
            if friends[i][j] == 1:
                self.dfs(friends, j, visited)

    def findCircleNum(self, friends: List[List[int]]) -> int:
        visited = set()
        circles = 0

        for i in range(len(friends)):
            if i not in visited:
                self.dfs(friends, i, visited)
                circles += 1

        return circles


s = Solution()
M = [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 1]]
print(s.findCircleNum(M))

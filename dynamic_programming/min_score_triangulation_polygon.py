'''
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.
For each triangle, the value of that triangle is the product of the labels of the vertices,
and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
'''


from typing import List


#   we fix edge [end, st] and try to build triangles through other vertexes
#   merge intervals dp pattern
class Solution:
    def recursive_score(self, arr, st, end, memo):
        if end - st < 2:
            return 0

        if (st, end) in memo:
            return memo[(st, end)]

        min_res = float('inf')
        for i in range(st + 1, end):
            cur_mult = arr[st] * arr[end] * arr[i]
            c1 = self.recursive_score(arr, st, i, memo)
            c2 = self.recursive_score(arr, i, end, memo)
            min_res = min(min_res, c1 + cur_mult + c2)

        memo[(st, end)] = min_res
        return min_res

    def minScoreTriangulation(self, arr: List[int]) -> int:
        return self.recursive_score(arr, 0, len(arr) - 1, {})


solution = Solution()
arr = [7, 3, 2, 6, 1]
print(solution.minScoreTriangulation(arr))

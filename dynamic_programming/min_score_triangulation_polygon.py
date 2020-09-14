from typing import List


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

from typing import List


class Solution:
    def min_diff_helper(self, job_difficulty, d, i, j, memo):
        if i > j:
            return 0
        if d == 0:
            return max(job_difficulty[i: j + 1])

        if (d, i, j) in memo:
            return memo[(d, i, j)]

        min_res = float('inf')
        cost = 0
        for k in range(i, j - (d - 1) + 1):
            cost = max(cost, job_difficulty[k])
            res = self.min_diff_helper(job_difficulty, d - 1, k + 1, j, memo) + cost
            min_res = min(min_res, res)

        memo[(d, i, j)] = min_res
        return min_res

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        return self.min_diff_helper(jobDifficulty, d, 0, len(jobDifficulty) - 1, {})

solution = Solution()
jobDifficulty = [6,5,4,3,2,1]
d = 2
print(solution.minDifficulty(jobDifficulty, d))

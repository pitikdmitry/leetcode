class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1


solution = Solution()
start_fuel = 10
target = 50
stations = [[1, 10], [2, 10], [3, 20], [4, 50]]
print(solution.minRefuelStops(target, start_fuel, stations))

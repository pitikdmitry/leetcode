'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
from collections import Counter


class Solution:
    def update_min_window_length(self, min_window_start: int, min_window_end: int, slow: int, fast: int) -> tuple:
        cur_window_length = fast - slow + 1
        min_window_length = min_window_end - min_window_start + 1
        if cur_window_length < min_window_length:
            min_window_start = slow
            min_window_end = fast

        return min_window_start, min_window_end

    def minWindow(self, s: str, t: str) -> str:
        slow, fast = 0, 0
        min_window_start, min_window_end = 0, float('inf')

        window_letters = Counter()
        t_letters = Counter(t)

        #   indicates if we have found all letters
        needed_letters = len(t_letters)

        while fast < len(s):

            #   increasing window size
            c = s[fast]
            if c in t_letters:
                window_letters[c] += 1

                if window_letters[c] == t_letters[c]:
                    needed_letters -= 1

            fast += 1

            #   reducing window size from the left side
            while slow < fast:
                c = s[slow]
                if c in window_letters and window_letters[c] > t_letters[c]:
                    window_letters[c] -= 1
                elif c in window_letters:
                    break

                slow += 1

            #   update window size, if we have found all letters
            if needed_letters == 0:
                min_window_start, min_window_end = self.update_min_window_length(min_window_start, min_window_end,
                                                                                 slow, fast - 1)

        if needed_letters > 0:
            return ''

        return s[min_window_start: min_window_end + 1]


solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))

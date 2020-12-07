'''
You are given an integer array A.  From some starting index, you can make a series of jumps.
The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.



Example 1:

Input: [10,13,12,14,15]
Output: 2
Explanation:
From starting index i = 0, we can jump to i = 2 (since A[2]
is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]),
then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4)
where we can reach the end with some number of jumps.
'''


from typing import List


#   The problem is how to find next greater element in array, that is righter
#   We will use decreasing stack and process elements in sorted order
class Solution:
    def build_next_greater_el_array(self, increasing_elements_idxs, next_bigger_el_idxs):
        decr_stack = []
        for idx in increasing_elements_idxs:
            while len(decr_stack) > 0 and decr_stack[-1] < idx:
                prev_idx = decr_stack.pop()
                next_bigger_el_idxs[prev_idx] = idx

            decr_stack.append(idx)

    def oddEvenJumps(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        arr_with_idx = [[arr[i], i] for i in range(len(arr))]

        #   for next bigger element
        arr_with_idx_sorted = sorted(arr_with_idx, key=lambda x: x[0])
        increasing_elements_idxs = list(map(lambda x: x[1], arr_with_idx_sorted))
        next_bigger_el_idxs = [None for i in range(len(arr))]
        self.build_next_greater_el_array(increasing_elements_idxs, next_bigger_el_idxs)

        #   for next smaller element
        arr_with_idx_sorted_desc = sorted(arr_with_idx, key=lambda x: x[0], reverse=True)
        increasing_elements_idxs_desc = list(map(lambda x: x[1], arr_with_idx_sorted_desc))
        next_smaller_el_idxs = [None for i in range(len(arr))]
        self.build_next_greater_el_array(increasing_elements_idxs_desc, next_smaller_el_idxs)

        #   process elements
        higher = [False for i in range(len(arr))]
        lower = [False for i in range(len(arr))]

        higher[-1] = True
        lower[-1] = True

        result = 1
        for i in range(len(arr) - 2, -1, -1):
            next_bigger_el_idx = next_bigger_el_idxs[i]
            next_smaller_el_idx = next_smaller_el_idxs[i]

            if next_bigger_el_idx is not None:
                lower[i] = higher[next_bigger_el_idx]
            if next_smaller_el_idx is not None:
                higher[i] = lower[next_smaller_el_idx]

            if lower[i] is True:
                result += 1

        return result


solution = Solution()
arr = [10,13,12,14,15]
print(solution.oddEvenJumps(arr))

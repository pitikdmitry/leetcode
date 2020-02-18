'''
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = 1
        r = n

        while l <= r:
            current = int(((l - r) / 2) + r)
            next = current + 1

            if next == n + 1:
                if not isBadVersion(current):
                    return current
                else:
                    r = current - 1
            if not isBadVersion(current) and isBadVersion(next):
                return next
            elif isBadVersion(current) and isBadVersion(next):
                r = current - 1
            else:
                l = current + 1

        return 1

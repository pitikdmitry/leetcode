'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]

Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:
Input:
asteroids = [8, -8]
Output: []

Explanation:
The 8 and -8 collide exploding each other.

Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]

Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
'''


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        prev = 0
        cur = 1

        while cur < len(asteroids):
            if prev < 0:
                prev = 0
                cur = 1
                continue

            ast_prev = asteroids[prev]
            ast_cur = asteroids[cur]

            if ast_prev >= 0 and ast_cur <= 0:
                if abs(ast_prev) == abs(ast_cur):
                    asteroids.pop(cur)
                    asteroids.pop(prev)
                    prev -= 1
                    cur -= 1
                    continue
                elif abs(ast_prev) > abs(ast_cur):
                    asteroids.pop(cur)
                    continue
                else:
                    asteroids.pop(prev)
                    prev -= 1
                    cur -= 1
                    continue
            else:
                prev += 1
                cur += 1

        return asteroids


s = Solution()
asteroids = [11, 10, 5, -5, -7, -18]
print(s.asteroidCollision(asteroids))

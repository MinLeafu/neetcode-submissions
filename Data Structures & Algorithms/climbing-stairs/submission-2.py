class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        one, two = 1, 2
        for i in range(n - 2):
            curr = one + two
            one = two
            two = curr
        return curr
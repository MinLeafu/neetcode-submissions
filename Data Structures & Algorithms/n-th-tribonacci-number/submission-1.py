class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        T0, T1, T2 = 0, 1, 1
        for _ in range(n - 2):
            T0, T1, T2 = T1, T2, T0 + T1 + T2
        return T2
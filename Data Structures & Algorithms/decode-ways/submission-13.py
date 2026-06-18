class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if int(s[0]) != 0 else 0

        left = 1
        right = 1 if int(s[0]) != 0 else 0
        for i in range(1, n):
            temp = 0
            if int(s[i]) != 0:
                temp += right
            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                temp += left
            left, right = right, temp
        return right
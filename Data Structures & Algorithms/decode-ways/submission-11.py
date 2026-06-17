class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if int(s[0]) != 0 else 0

        left = 1 if int(s[0]) != 0 else 0
        right = 0
        if int(s[1]) != 0:
            right += left
        if 10 <= int(s[0:2]) <= 26:
            right += 1

        for i in range(2, n):
            temp = 0
            if int(s[i]) != 0:
                temp += right
            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                temp += left
            left, right = right, temp
        return right
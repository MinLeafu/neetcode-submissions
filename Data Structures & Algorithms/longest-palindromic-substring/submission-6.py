class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        longest, res = 0, ""
        for i in range(n - 1):
            l = r = i
            length = 1
            while True:
                l -= 1
                r += 1
                if l < 0 or r > n - 1 or s[l] != s[r]:
                    break
                length += 2
            if length > longest:
                longest = length
                res = s[l + 1:r]

            l, r = i + 1, i
            length = 0
            while True:
                l -= 1
                r += 1
                if l < 0 or r > n - 1 or s[l] != s[r]:
                    break
                length += 2
            if length > longest:
                longest = length
                res = s[l + 1:r]
        return res
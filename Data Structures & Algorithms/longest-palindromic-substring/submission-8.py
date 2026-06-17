class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        longest, res = 0, ""
        for i in range(n - 1):
            l = r = i
            while True:
                l -= 1
                r += 1
                if l < 0 or r > n - 1 or s[l] != s[r]:
                    break
            if r - l + 1 > longest:
                longest = r - l + 1
                res = s[l + 1:r]

            l, r = i + 1, i
            while True:
                l -= 1
                r += 1
                if l < 0 or r > n - 1 or s[l] != s[r]:
                    break
            if r - l + 1 > longest:
                longest = r - l + 1
                res = s[l + 1:r]
        return res
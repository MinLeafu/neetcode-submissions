class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        longest, res = 0, ""
        for i in range(n - 1):
            l = r = i
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > longest:
                longest = r - l + 1
                res = s[l + 1:r]

            l, r = i + 1, i
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > longest:
                longest = r - l + 1
                res = s[l + 1:r]
        return res
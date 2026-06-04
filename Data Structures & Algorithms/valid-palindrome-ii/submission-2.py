class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if self.isPalindrome(s, l + 1, r):
                    return True
                elif self.isPalindrome(s, l, r - 1):
                    return True
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
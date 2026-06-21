class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if dp[i - 1]:
                for word in wordDict:
                    if i + len(word) - 1 <= n and s[i - 1:i + len(word) - 1] == word:
                        dp[i + len(word) - 1] = True
        return dp[n]
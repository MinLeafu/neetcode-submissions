class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(prefix)):
                if j == len(strs[i]) or prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix
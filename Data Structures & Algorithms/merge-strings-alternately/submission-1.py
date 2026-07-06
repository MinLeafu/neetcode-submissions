class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr = 0
        res = []

        while ptr < len(word1) and ptr < len(word2):
            res.append(word1[ptr])
            res.append(word2[ptr])
            ptr += 1
        
        res.append(word1[ptr:])
        res.append(word2[ptr:])
        
        return "".join(res)
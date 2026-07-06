class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr = 0
        res = ""
        
        while ptr < len(word1) and ptr < len(word2):
            res += word1[ptr]
            res += word2[ptr]
            ptr += 1
        
        while ptr < len(word1):
            res += word1[ptr]
            ptr += 1
        
        while ptr < len(word2):
            res += word2[ptr]
            ptr += 1
        
        return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for str in strs:
            chars = [0] * 26
            for char in str:
                chars[ord(char) - ord('a')] += 1
            chars = tuple(chars)

            if chars in hashmap:
                hashmap[chars].append(str)
            else:
                hashmap[chars] = [str]

        return [x for x in hashmap.values()]
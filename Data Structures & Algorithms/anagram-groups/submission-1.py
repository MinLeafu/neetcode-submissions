class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            if "".join(sorted(str)) in hashmap:
                hashmap["".join(sorted(str))].append(str)
            else:
                hashmap["".join(sorted(str))] = [str]
        return [x for x in hashmap.values()]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp in hash:
                hash[temp].append(s)
            else:
                hash[temp] = [s]
        return list(hash.values())
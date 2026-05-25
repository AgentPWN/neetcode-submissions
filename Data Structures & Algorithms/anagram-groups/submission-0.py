class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sup = []
        final = []
        for i in strs:
            for j in strs:
                if ''.join(sorted(i)) == ''.join(sorted(j)):
                    sup.append(j)
            if sup not in final:
                final.append(sup)
            sup = []
        return final
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slop = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in slop:
                l = max(l, slop[s[r]] + 1)
            slop[s[r]] = r
            res = max(res, r - l + 1)

        return res
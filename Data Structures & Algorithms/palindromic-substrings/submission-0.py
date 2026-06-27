class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        resLen = 0
        count = 0
        def check(l,r,n):
            nonlocal res
            nonlocal resLen
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1


        n = len(s)
        for i in range(len(s)):
            check(i,i,n)
            check(i,i+1,n)
        return count
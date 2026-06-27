class Solution:

    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        def check(l,r,n):
            nonlocal res
            nonlocal resLen
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l +1
                l -= 1
                r += 1


        n = len(s)
        for i in range(len(s)):
            check(i,i,n)
            check(i,i+1,n)
        return res
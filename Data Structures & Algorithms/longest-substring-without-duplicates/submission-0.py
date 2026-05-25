class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 1
        n = len(s)
        for i in range(n-length+1):
            while i+length <= n:
                if len(s[i:i+length]) == len(set(s[i:i+length])):
                    length += 1
                else:
                    break
        return length - 1
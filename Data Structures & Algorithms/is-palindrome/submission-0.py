import re, string
pattern = re.compile('[\W_]+')
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = pattern.sub('', s)
        if x == x[::-1]:
            return True
        else:
            return False
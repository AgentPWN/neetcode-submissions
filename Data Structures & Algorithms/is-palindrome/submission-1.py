class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                string += i
        return string == string[::-1]
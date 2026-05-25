class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs != []:
            a = ";".join(strs)
            return a
        else:
            return []
    def decode(self, s: str) -> List[str]:
        if s != []:
            a = s.split(";")
            return a
        else:
            return []
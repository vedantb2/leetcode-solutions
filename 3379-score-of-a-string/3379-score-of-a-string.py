class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(0, len(s)-1):
            x = ord(s[i]) - ord(s[i+1])
            x = abs(x)
            result += x
        return result
        
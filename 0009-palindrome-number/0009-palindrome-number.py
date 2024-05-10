class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        rString = ""
        for i in range(len(string)-1, -1, -1):
            rString += string[i]
        return string == rString
        # if x < 0: return False
        # reversed_a = a.copy()
        # reversed_a.reverse()
        # return a == reversed_a
    
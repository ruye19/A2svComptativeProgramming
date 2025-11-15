class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = list(s)
        for i in range(len(s)):   
            s[i] = 1 if s[i] == "R" else -1 

        for j in range(1, len(s)):
            s[j] += s[j - 1]
        return s.count(0)    


   
        
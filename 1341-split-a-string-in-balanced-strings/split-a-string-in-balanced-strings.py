class Solution:
    def balancedStringSplit(self, s: str) -> int:
        summ = 0
        count = 0
        for j in range(len(s)):
            summ += 1 if s[j] == "R" else -1 
            if summ == 0:
                count += 1 
        return count   


   
        
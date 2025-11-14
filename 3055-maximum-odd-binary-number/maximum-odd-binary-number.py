class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        si = ["0"] * len(s)
        si[-1] = "1"
        ones -= 1
        for i in range(ones):
            si[i] = "1"
        return "".join(si)    
        
            
            
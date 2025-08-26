class Solution:
    def minimumSteps(self, s: str) -> int:
        z = 0
        count = 0
        for i in range(len(s)):
            if s[i] == "0":
                count += (i - z)
                z += 1
        return count            

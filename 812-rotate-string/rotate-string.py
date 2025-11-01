class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        s = list(s)
        for i in range(len(s)):
            s.append(s.pop(0))
            if "".join(s) == goal:
                return True
        return False

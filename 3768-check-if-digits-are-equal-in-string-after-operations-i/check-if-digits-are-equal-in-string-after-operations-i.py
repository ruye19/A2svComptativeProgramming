class Solution:
    def hasSameDigits(self, s: str) -> bool:
        si=""
        while(len(s)>2):
            si=""
            for i in range(len(s)-1):
                si += str((int(s[i]) + int(s[i+1]))% 10)
            s=si
        print(s)
        if s[0]==s[1]:
            return True
        return False        
        
               
        # si = ""
        # i = 0
        # while len(s)-1 > i and len(s) > 2:
        #     si += str((int(s[i]) + int(s[i+1]))% 10)
        #     i += 1
        #     print(si)



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=0
        tList=list(t)
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            if s[i] in tList:
                tList.remove(s[i])
                count+=1
        if count==len(s):
            return True
        else:
            return False    

        
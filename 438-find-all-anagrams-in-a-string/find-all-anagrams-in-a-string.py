class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pcounter = defaultdict(int)
        scounter=defaultdict(int)
        if len(s)<len(p):
            return []
        for i in range(len(p)):
            pcounter[p[i]]+=1
            scounter[s[i]]+=1
        res=[0] if pcounter==scounter else []  
        l=0
        for r in range(len(p),len(s)):
            scounter[s[r]]+=1
            scounter[s[l]]-=1
            if scounter[s[l]]==0:
               scounter.pop(s[l])
            l+=1
            if scounter ==pcounter:
               res.append(l)    
        return res 

        
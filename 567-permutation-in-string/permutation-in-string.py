class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Counter = defaultdict(int)
        s2Counter = defaultdict(int)
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1Counter[s1[i]]+=1
            s2Counter[s2[i]]+=1
        if s1Counter == s2Counter:
            return True 
        l=0
        for r in range(len(s1),len(s2)):
            s2Counter[s2[r]]+=1
            s2Counter[s2[l]]-=1

            if s2Counter[s2[l]]==0:
                s2Counter.pop(s2[l])
            l+=1   
            if s2Counter==s1Counter:
                return True
        return False         




        
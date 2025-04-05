class Solution(object):
    def findMaxAverage(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        window=sum(s[:k])
        left=0
        maxx=window
        for r in range(k,len(s)):
            window= window-s[left] +s[r] 
            left+=1
            maxx=max(window,maxx)
        return float(maxx)/k   
        
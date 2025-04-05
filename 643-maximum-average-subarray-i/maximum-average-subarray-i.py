class Solution(object):
    def findMaxAverage(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        window=sum(s[:k])
        maxx=window
        for r in range(k,len(s)):
            window= window- s[r-k] + s[r] 
            maxx=max(window,maxx)
        return float(maxx)/k   
        
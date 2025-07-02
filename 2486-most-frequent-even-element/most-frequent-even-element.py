class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count ={}
        freq=[[] for i in range(len(nums)+1)]
    
        for j in nums:
            count[j]= 1 + count.get(j,0)
        for num,countt in  count.items():
            freq[countt].append(num)
        even=False    
        for c in range(len(freq)-1,0,-1):
            for f in sorted(freq[c]):
                if f%2==0:
                    even=True
                    return f
        if not even:
            return -1            



        
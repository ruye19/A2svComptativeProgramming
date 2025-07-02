class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count ={}
        freq=[[] for i in range(len(nums)+1)]
        output=[]
        for j in nums:
            count[j]= 1 + count.get(j,0)
        for num,countt in  count.items():
            freq[countt].append(num)
        for c in range(len(freq)-1,0,-1):
            for f in freq[c]:
                output.append(f)
                if len(output)==k:
                    return output   



        
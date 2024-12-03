class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefixsum = 0
        count = 0
        prefixsumm = {0: 1} 

        for i in range(n): 
            prefixsum += nums[i]  
           
            if (prefixsum - k) in prefixsumm:
                count += prefixsumm[prefixsum - k]  
            if prefixsum in prefixsumm:
                prefixsumm[prefixsum] += 1
            else:
                prefixsumm[prefixsum] = 1

        return count  
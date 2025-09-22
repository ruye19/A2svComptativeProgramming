class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0 for _ in range(len(nums))]
        for i, j in requests:
            count[i] += 1
            if j + 1 < len(count):
               count[j + 1] -= 1

        for i in range(1,len(count)):
            count[i] += count[i - 1]   

        total = 0
        for i,j in zip(sorted(nums),sorted(count)):
            total += i * j
        return total % (10**9 + 7)    
                     
        
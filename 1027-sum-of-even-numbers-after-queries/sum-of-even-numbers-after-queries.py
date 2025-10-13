class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        even = sum(num for num in nums if num % 2 == 0)
        for val,index in queries:
            if nums[index] % 2 == 0:
                even -= nums[index]

            nums[index] += val
            if nums[index] % 2 == 0:
                even += nums[index]
            output.append(even)    
        
        return output        
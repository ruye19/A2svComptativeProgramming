class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxx = max(nums)
        countArray = [0] * (maxx + 1)
        output = []
        for num in nums:
            countArray[num] += 1
        # print(countArray) 
        for i in range(1,len(countArray)):
            countArray[i] += countArray[i - 1]
        # print(countArray) 
        for num in nums:
            if num == 0:
                output.append(0)
            else:    
                output.append(countArray[num - 1])

        return output   



        return []



        
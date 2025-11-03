class Solution:
    def numberOfBeams(self, bank: List[str]) -> int: 
        nums = []
        for row in bank:
            count = sum(map(int, list(row)))
            if count != 0:
                nums.append(count) #row.count('1')
        result = 1
        output= 0        
        for i in range(len(nums) -1 ):
            result = nums[i] * nums[i + 1]
            output += result
        return output
        
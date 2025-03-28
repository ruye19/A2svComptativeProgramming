class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first,second = 0,len(numbers)-1
       
        while(second < len(numbers)):
            summ=numbers[first] + numbers[second]
            if (summ == target):
               return [first+1,second+1]
            elif(summ< target):
                first=first+1
            else:
                second=second-1
        return [first+1,second+1] 


        
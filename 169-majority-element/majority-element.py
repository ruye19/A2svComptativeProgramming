class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=0
        count = defaultdict(int)
        for i in nums: 
            count[i]+=1
        element=max(count,key=count.get)
        return element
                



        
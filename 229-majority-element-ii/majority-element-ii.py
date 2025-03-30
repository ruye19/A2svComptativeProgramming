class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elements=defaultdict(int)
        solution=[]  
        n= len(nums) 
        for num in nums:
            elements[num]+=1
        thresld=n//3   
        for key, count in elements.items():    
            if count > thresld:
                solution.append(key)
        return solution    



class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
    
        length_1 = len(nums1)
        length_2 = len(nums2)
        xor_1 = xor_2 = 0
        if length_2 % 2 != 0:
            
            for i in nums1:
                xor_1 ^= i 
                
        if length_1 % 2 != 0:
          
            for i in nums2:
                xor_2 ^= i 
        return xor_2 ^ xor_1
            
             
       
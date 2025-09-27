class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        nums1 = [2, 1, 3] nums2 = [10, 2, 5, 0]
        
        
        nums3 = [2 XOR 10, ..... 1 XOR 10, ..... 3 XOR 10]
        
        for 2: 
            10 XOR 2 XOR  5 XOR 0
            
            
        for 1: 
            10 XOR 2 XOR  5 XOR 0
            
        for 3: 
            10 XOR 2 XOR  5 XOR 0
       
            
        """
        
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
            
                
        """
        orr what dont we use the same variable koy 1 2
        
        what is happing to you koyyy 
        mnew ee
        lmfaoooo
        i heard tiktok u guys lossss yeahhhhhhh w
        where was my reactions thadiya
        i cant lol fr lollll 
        wyzoh beka next arsenal siyashenf desta bedesta enhonaleh
        
        yeah so bemn lnseraw new 2 loop?
        the last one what did u say 
        yeah the idea i guess i am okay with it buttt idk how the implemtaion 
        
        
        total = 0
        for num in nums:
            total = total ^ num
        eshi yeah 
        
        ltmot new dont confuse me 
        
        [2, 1, 3]    [10, 2, 5, 0]
        0              13
        
        
        [1, 2, 3]  [6, 4, 5]
       0 ^ 0 ^ 0          7 ^ 7 ^ 7
        
        1: 1^6 ^ 1^4 ^ 1^5  = 1 ^ (6^4^5)
        
        2: 2^6, 2^4, 2^5 = 2 ^ (6^4^5)
        3: 3^6, 3^4, 3^5 = 3 ^ (6^4^5)
         
        1111 yeah even kehone 0 new leza we only need to do if the len is odd i mean for the oppsite ig eshi look up i done smthing  ...melata :)
        
        """
        print(1 ^ 2 ^ 3 ^ 6 ^ 4 ^ 5)
       
        return 0
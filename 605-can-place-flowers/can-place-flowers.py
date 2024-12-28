from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
               
                prev = 0 if i == 0 else flowerbed[i - 1]
                next = 0 if i == length - 1 else flowerbed[i + 1]
                
                if prev == 0 and next == 0:  
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:  
                       return True
        
        return count>=n

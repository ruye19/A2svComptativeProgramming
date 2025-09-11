class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        def distribute(c: int) -> bool:
            if c == 0:
                return True
            
            count = 0
            for cc in candies:
                count += cc // c
                if count >= k:
                    return True
            return False

        left, right = 0, sum(candies)
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if distribute(mid):
                left = mid
            else:
                right = mid - 1
                
        return left
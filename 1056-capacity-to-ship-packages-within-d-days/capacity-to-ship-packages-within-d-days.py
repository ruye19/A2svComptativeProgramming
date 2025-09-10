class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            total = 0 
            d = 1
            for i in range(len(weights)):
                if total + weights[i] > capacity:
                    d += 1
                    total = weights[i]
                else:
                    total += weights[i]    
            return d <= days 
    
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left             

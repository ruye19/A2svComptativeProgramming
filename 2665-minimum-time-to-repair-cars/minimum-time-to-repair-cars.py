class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def number_cars(t):
            total = 0
            for r in ranks:
                n = int(sqrt(t / r))
                total += n
            return total 

        left, right = 1, ranks[0] * cars * cars
    
        while left <= right:
            mid = (left + right) // 2
            if number_cars(mid) >= cars:
            
                right = mid - 1
            else:
                left = mid + 1 
        return right + 1                

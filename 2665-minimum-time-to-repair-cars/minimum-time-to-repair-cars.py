class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def number_cars(t):
            total = 0
            for r in ranks:
                n = int(sqrt(t / r))
                total += n
            return total 

        left, right = 1, ranks[0] * cars * cars
        res = -1 
        while left <= right:
            mid = (left + right) // 2
            if number_cars(mid) >= cars:
                res = mid
                print(res)
                right = mid - 1
            else:
                left = mid + 1 
        return res                 

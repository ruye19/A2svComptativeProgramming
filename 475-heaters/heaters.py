class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def closest(houses, heaters):
            left, right = 0, len(heaters) - 1
            min_distance = float('inf')
            while left <= right:
                mid = (left + right) // 2
                min_distance = min(min_distance, abs(heaters[mid] - houses))
                if heaters[mid] < houses:
                    left = mid + 1 
                else:
                    right = mid - 1
            return min_distance  

        radius = 0 
        heaters = sorted(heaters)
        for house in houses:
            radius = max(radius, closest(house, heaters))
        return radius    

       
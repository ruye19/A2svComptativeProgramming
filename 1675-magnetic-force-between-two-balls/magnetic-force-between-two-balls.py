class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_distribute(mi,balls):
            count = 1
            prev = 0
            for i in range(len(position)):
                if position[i] - position[prev] >= mi:
                    count += 1
                    prev = i
            return count >= balls 
        position = sorted(position)     
        left, right = 0, max(position)
        while left <= right:
            mid = (right + left) // 2
            if can_distribute(mid, m):
                left = mid + 1
            else:
                right = mid - 1   
        return left - 1   



        
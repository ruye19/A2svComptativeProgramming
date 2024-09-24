class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        intersectt= set(nums[0])
        for i in nums[1:]:
            i= set(i)
            intersectt.intersection_update(i)
            
        return sorted(list(intersectt))

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dif=set(nums1)
        diff=set(nums2)
        diff.difference_update(set(nums1))
        dif.difference_update(set(nums2))
        return [dif,diff]

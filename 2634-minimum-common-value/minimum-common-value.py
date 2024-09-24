class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
      intersect=set(nums1)
      ans=intersect.intersection(set(nums2))
      
      ans=sorted(ans)
      
      if not ans:
        return -1
      return ans[0]  
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect=[]
        len1=len(nums1)
        len2=len(nums2)
        for i in range (len1):
            if nums1[i] in nums2:
                intersect.append(nums1[i])
        for i in range (len2):
            if nums2[i] in nums1:
                intersect.append(nums2[i])  
        return list(set(intersect))               
                 


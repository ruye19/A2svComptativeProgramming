class Solution(object):
    def findDifference(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
    
        set1= set(num1)
        set2= set(num2)
        return [list(set1-set2),list(set2-set1)]       
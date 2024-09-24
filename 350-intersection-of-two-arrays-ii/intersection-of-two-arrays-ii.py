from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)  # Count occurrences in nums1
        intersection = []
        
        for num in nums2:
            if counts[num] > 0:  # If num is in nums1
                intersection.append(num)
                counts[num] -= 1  # Decrement the count
        
        return intersection

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []

        # Process nums2 from left to right
        for num in nums2:
            # Pop smaller elements and map them to the current num (which is greater)
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For remaining elements in the stack, no next greater
        while stack:
            next_greater[stack.pop()] = -1

        # Build output for nums1 based on mapping
        return [next_greater[num] for num in nums1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        def first(nums, target):
            left = 0
            right = len(nums) - 1
            first_occurrence = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurrence = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:  
                    right = mid - 1
            return first_occurrence

        def last(nums, target):
            left = 0
            right = len(nums) - 1
            last_occurrence = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurrence = mid
                    left = mid + 1 
                elif nums[mid] < target:
                    left = mid + 1
                else: 
                    right = mid - 1
            return last_occurrence

        return [first(nums, target), last(nums, target)]
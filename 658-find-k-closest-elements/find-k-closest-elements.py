class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        
        # Reduce the window until the number of elements between left and right is exactly k
        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1  # Remove the element at left
            else:
                right -= 1  # Remove the element at right
        
        # The window [left, right] now contains the k closest elements
        return arr[left:right+1]

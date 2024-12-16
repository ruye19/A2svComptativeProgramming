class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        area=0
        left=0
        right=n-1
        while left<right:
            curArea=(right-left) *(min(height[left],height[right]))
            area=(max(area,curArea))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1    
        return area

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        while left < right:
            md = left+(right-left)//2
            if isBadVersion(md):
                right=md
            else:
                left=md+1
        return left            
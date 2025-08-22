class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        res = 0
        left, right = 0, n - 1
        while left < right:
            res += piles[right - 1]
            left += 1
            right -= 2
        return res

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Sum the first k elements
        summ = sum(cardPoints[:k])
        maxSum = summ
        
        # Sliding window
        for i in range(1, k + 1):
            summ = summ - cardPoints[k - i] + cardPoints[-i]
            maxSum = max(maxSum, summ)
        
        return maxSum


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0 for i in range(k)]
        for num in arr:
            freq[num % k] += 1
        for num in range(1, k):
            if num == k - num and freq[num] & 1:
                return False
            if freq[num] != freq[k - num]:
                return False
        return True            

        
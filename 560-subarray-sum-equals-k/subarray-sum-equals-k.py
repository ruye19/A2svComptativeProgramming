class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = nums
        for i in range(1 , len(nums)):
            prefix[i] += prefix[i - 1]
        hashmap = {0 : 1}
        result = 0 
        for p in prefix:
            target = p - k
            result += hashmap.get(target, 0)
            hashmap[p] = hashmap.get(p, 0) + 1
        return result         
        
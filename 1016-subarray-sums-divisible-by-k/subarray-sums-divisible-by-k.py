class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        result = 0 
        hashmap = {0 : 1}
        for n in nums:
            prefix += n
    
            target = prefix % k
            result += hashmap.get(target, 0)
            hashmap[target] = 1 + hashmap.get(target, 0)
        return result         
             
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_dict = defaultdict(int)
        pair_dict = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i] * nums[j]
                pair_dict[prod] += prod_dict[prod]
                prod_dict[prod] += 1
        count = 0
        for item in pair_dict.values():
            count += 8*item
        return count              

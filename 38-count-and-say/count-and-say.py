class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(nums):
            pairs=[]
            l = 0
            while l < len(nums):
                r = l
                while r < len(nums) and nums[r] == nums[l]:
                    r += 1
                pairs.append([int(nums[l]), r - l]) 
                l = r   
            return pairs
        def Arrpairs(pair):
            res = ""
            for num, freq in pair:
                res += str(freq) + str(num)
            return res
        result = "1"
        for i in range(n - 1):
           s = helper(result)
           result = Arrpairs(s)
        return result   


        
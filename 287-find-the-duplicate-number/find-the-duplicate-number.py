class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
          count[num]+=1
        for key ,coun in count.items():
            if coun>=2:
                return key    
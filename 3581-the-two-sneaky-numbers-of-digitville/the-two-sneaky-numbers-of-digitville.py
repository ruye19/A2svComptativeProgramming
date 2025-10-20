class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []
        freq = Counter(nums)
        for items,count in freq.items():
            if count >= 2:
                output.append(items)
        return output         


        
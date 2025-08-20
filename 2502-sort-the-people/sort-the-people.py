class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
                    
        hashnames = defaultdict(list)
        for name, height in zip(names, heights):
            hashnames[height].append(name)
            
        countArray = [0 for _ in range(max(heights) + 1)]
        for height in heights:
            countArray[height] += 1
            
        result = []
        for i in range(len(countArray) - 1, -1, -1):
            if countArray[i]:
                result.extend(hashnames[i])
            
        return result
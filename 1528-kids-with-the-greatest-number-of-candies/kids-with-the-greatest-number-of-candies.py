class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxx=0
        for i in range(len(candies)):
            maxx=max(maxx,candies[i])
        for i in range(len(candies)):
            candiN=candies[i]+extraCandies 
            if candiN>=maxx:
                result.append(True)
            else:
                result.append(False)
        return result            
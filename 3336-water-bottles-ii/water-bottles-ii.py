class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        empty = numBottles 
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            empty += 1
            fullBottles += 1
        return fullBottles    

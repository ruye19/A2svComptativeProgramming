class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            Exchange = 1                   
            numBottles -= numExchange       
            total += Exchange
            numBottles += Exchange         
            numExchange += 1               

        return total

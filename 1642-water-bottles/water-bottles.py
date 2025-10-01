class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
      
        while numBottles >= numExchange:
            Exchange = numBottles // numExchange
            xtras = numBottles % numExchange
            total += Exchange
            numBottles = Exchange + xtras
        return total     
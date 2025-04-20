class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=prices[0]
        profit=0
        for price in prices[1:]:
            if price < min_buy:
                min_buy=price
            else:    
                current_profit=price- min_buy   
                if(current_profit > profit):
                    profit=current_profit
        return profit        


        
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        losers = []

        for match in matches:
            winners.append(match[0])
            losers.append(match[1]) 
        # print(winners , losers) 

        counts = Counter(losers)
        
        winner = {i for i in winners if counts[i] == 0}
        loser = {j for j in losers if counts[j] == 1}   
           
        return [sorted(winner),sorted(loser)]

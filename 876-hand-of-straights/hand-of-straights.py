class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # Count your hand
        cards = Counter(hand)
        # start from the minimum card
        #values
        values = list(set(hand))
        values.sort()   
        
        minIndex = 0  
        while cards:
            
            for i in range(groupSize):
                if values[minIndex] + i not in cards:
                    return False
                else:
                    cards[values[minIndex] + i] -= 1
                    if cards[values[minIndex] + i] == 0:
                        del cards[values[minIndex] + i]
            
            while minIndex != len(values) and values[minIndex] not in cards:
                minIndex += 1
            
        return True
            
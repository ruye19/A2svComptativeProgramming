class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindx = {}
        for i,c in enumerate(s):
            lastindx[c] = i
        end = 0  
        count = 0  
        output = []
        for i,c in enumerate(s):
            count += 1
            end=max(end,lastindx[c])
            if end == i:
                output.append(count)
                count = 0
        return output        

        
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        adjList = defaultdict(set)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adjList[i].add(j)
                    
        """
        {
            1: [2, 3]
            2: [2, 4] + [2, 3]
        }
        """
                                    
        for node in adjList:
            for neighbor in adjList[node]:
                adjList[neighbor] = adjList[neighbor].union(adjList[node])
        print(adjList)
        output = set()
        for node, neig in adjList.items():
            neig = list(neig)
            neig.sort()
            output.add(tuple(neig))
        return len(output)    
            
            
    
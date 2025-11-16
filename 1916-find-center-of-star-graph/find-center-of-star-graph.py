class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        indegree = [0 for _ in range(len(edges) + 1)]
        for u, v in edges:
            indegree[u - 1] += 1
            indegree[v - 1] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == len(edges):
                return i + 1
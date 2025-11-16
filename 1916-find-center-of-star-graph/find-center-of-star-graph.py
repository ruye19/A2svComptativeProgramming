class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        u, v = edges[0]
        if u in edges[1]:
            return u
        else:
            return v
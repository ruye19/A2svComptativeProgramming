class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True

        grp=defaultdict(list)
        for i , j in edges:
            grp[i].append(j)
            grp[j].append(i)

        visited=set()
        visited.add(source)
        q = deque()
        q.append(source)
        while q:
            node= q.popleft()
            if node==destination:
                return True
            for i in grp[node]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)       
        return False           

        
        
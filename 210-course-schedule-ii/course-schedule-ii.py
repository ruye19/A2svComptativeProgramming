class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        visited,unvisted,visiting=2,0,1
        state = [unvisted] * numCourses 
        def dfs(i):
            if state[i]==visiting:
                return False
            if state[i]==visited:
                return True
            state[i]=visiting
            for n in graph[i]:
                if not dfs(n):
                    return False
            state[i]=visited
            order.append(i)
            return True                

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order                 
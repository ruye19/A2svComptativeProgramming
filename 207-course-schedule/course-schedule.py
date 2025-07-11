class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=defaultdict(list)
        for a,p in prerequisites:
            graph[a].append(p)
        visited,unvisited,visiting=2,0,1    
        state=[0]*numCourses
        def dfs(i):
            if state[i]==visiting:
                return False
            elif state[i]==visited:
                return True 
            state[i]=visiting
            for ne in graph[i]:
                if not dfs(ne):
                    return False
            state[i]=visited 
            return True       


        for i in range(numCourses):
            if not dfs(i):
                return False
         
        return True

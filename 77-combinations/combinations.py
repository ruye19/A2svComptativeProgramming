class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path,ans=[],[]
        def backtracking(first_num):
            if len(path)==k:
                ans.append(path.copy())
                return 
          
            for candidate in range(first_num+1,n+1):
                path.append(candidate)
                backtracking(candidate)
                path.remove(candidate)
        backtracking(0)    
        return ans

        
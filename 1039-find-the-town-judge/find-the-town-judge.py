class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outside = defaultdict(int)
        inside = defaultdict(int)

        for u,v in trust:
            outside[u] += 1
            inside[v] += 1   

        for i in range(1, n + 1):
            if outside[i] == 0 and  inside[i] == n - 1:
                return i
        return -1        
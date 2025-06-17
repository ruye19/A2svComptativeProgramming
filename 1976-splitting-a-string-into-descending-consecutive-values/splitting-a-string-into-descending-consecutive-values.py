class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(index, prev):
            if index == len(s):
                return True
            for j in range(index + 1, len(s) + 1):
                val = int(s[index:j])
                if val + 1 == prev and dfs(j, val):
                    return True
            return False

        for i in range(1, len(s)):
            val = int(s[:i])
            if dfs(i, val):
                return True

        return False

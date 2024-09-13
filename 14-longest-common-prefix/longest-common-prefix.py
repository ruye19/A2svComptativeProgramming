from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with the rest of the strings
        for i in range(1, len(strs)):
            # Gradually reduce the prefix
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

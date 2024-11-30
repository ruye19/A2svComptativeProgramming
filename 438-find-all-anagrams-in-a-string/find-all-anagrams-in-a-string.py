class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        output = []
        n = len(p)
        p_count = Counter(p)  # Frequency of characters in p

        # Loop through all possible substrings of length n in s
        for i in range(len(s) - n + 1):
            # Extract the substring
            substring = s[i:i+n]
            
            # Check if it is an anagram of p
            if Counter(substring) == p_count:
                output.append(i)

        return output


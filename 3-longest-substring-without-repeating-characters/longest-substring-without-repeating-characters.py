class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the frequency of characters
        char_count = {}
        left = 0  # Left pointer of the sliding window
        max_length = 0  # To track the maximum length of a substring without repeating characters
        
        # Iterate over each character in the string using the right pointer `i`
        for right in range(len(s)):
            # Add/update the count of the current character
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # If we have a duplicate character, shrink the window from the left
            while char_count[s[right]] > 1:
                # Remove one occurrence of the character at the left pointer
                char_count[s[left]] -= 1
                left += 1  # Move the left pointer to the right to shrink the window
                
            # Update the max_length with the size of the current valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length



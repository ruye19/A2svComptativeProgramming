from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. Define the keypad mapping
        digit_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # 2. Initialize the list to store the final combinations
        result = []

        # 3. Handle the base case: an empty input string
        if not digits:
            return result

        # 4. Define the recursive (backtracking) helper function
        #    `index`: current digit being processed in the 'digits' string
        #    `current_path`: the list of characters forming the current combination
        def backtrack(index, current_path):
            # Base Case: If we've processed all digits
            if index == len(digits):
                result.append("".join(current_path)) # Convert list of chars to string
                return

            # Get the current digit and its corresponding letters
            current_digit = digits[index]
            letters = digit_map.get(current_digit, "") # Use .get() for safety, though constraints say 2-9

            # Iterate through each letter for the current digit
            for letter in letters:
                # Choose: Add the letter to the current combination
                current_path.append(letter)

                # Explore: Recurse for the next digit
                backtrack(index + 1, current_path)

                # Un-choose (Backtrack): Remove the last letter to try other options
                current_path.pop()

        # 5. Start the backtracking process from the first digit (index 0)
        #    and an empty starting combination list.
        backtrack(0, [])

        return result
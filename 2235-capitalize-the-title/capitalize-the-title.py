class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Split the title into individual words
        words = title.split()
        
        # Process each word
        for i in range(len(words)):
            if len(words[i]) > 2:
                # Capitalize the first letter and make the rest lowercase
                words[i] = words[i].capitalize()
            else:
                # Convert words with 2 or fewer letters to lowercase
                words[i] = words[i].lower()
        
        # Join the words back into a single string
        return ' '.join(words)

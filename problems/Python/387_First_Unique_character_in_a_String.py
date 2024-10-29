'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        
        # Iterate over the characters in the string with their indices
        for index, char in enumerate(s):
            # If the character's count is 1, it is unique
            if char_count[char] == 1:
                # Return the current index as the first unique character's position
                return index
      
        # If no unique character is found, return -1
        return -1
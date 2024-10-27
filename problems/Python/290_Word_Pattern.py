'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False

        word_index = 0
        match_map = {}

        for i in range(len(pattern)):
            print(i, word_index)
            if pattern[i] not in match_map:
                if words[word_index] in match_map.values():
                    return False

                match_map[pattern[i]] = words[word_index]
                word_index += 1
                continue

            elif match_map[pattern[i]] != words[word_index]:
                return False

            else:
                word_index += 1

        return True
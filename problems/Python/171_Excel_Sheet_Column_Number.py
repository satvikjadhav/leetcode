'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for i in range(len(columnTitle)):
            output *= 26
            output += (ord(columnTitle[i]) % 65) + 1 
        
        return output
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0  # Tracks the nesting level of parentheses
        result = ""  # Stores the final string without outer parentheses
        
        for p in s:
            if p == '(':  # Opening parenthesis
                balance += 1
                # Only add to result if this isn't the outermost '(' (balance > 1)
                if balance > 1:
                    result += p
            elif p == ')':  # Closing parenthesis
                balance -= 1
                # Only add to result if this isn't the outermost ')' (balance > 0 after decrement)
                if balance > 0:
                    result += p
        
        return result
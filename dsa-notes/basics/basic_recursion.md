# Basic Recursion

When a function calls itself until a specified condition is met. 

Base Condition: condition that is used to stop the recursion. 

Sample Code:

```python
def print_numbers(n):
    if n >= 1:
        print_numbers(n - 1)  # Recursive call
        print(n)               # Print the current number after returning from recursion
    else:
        return
    
# Example usage
n = 5
print_numbers(n)
```
Output:
1,
2,
3,
4,
5

Explanation:
- **Base Case**: The recursion stops when \( n < 1 \).
- **Recursive Call**: The function calls itself with \( n - 1 \) until it reaches the base case.
- **Print Statement**: After the recursive call, it prints the current value of \( n \), ensuring
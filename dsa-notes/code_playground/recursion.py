def print_numbers(n):
    if n >= 1:
        print_numbers(n - 1)  # Recursive call
        print(n)               # Print the current number after returning from recursion
    else:
        return
    
# Example usage
# print_numbers(5)

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)
# Example usage
# factorial(5)

# Sum of first N numbers
def sum_nums(n):
    if n == 1:
        return 1
    else:
        return n + sum_nums(n-1)

# print(sum_nums(10))

# Reverse an Array
def reverse_array(l,r):
    # recursion using 2 pointers
    if l >= r:
        return

    arr[l], arr[r] = arr[r], arr[l]

    reverse_array(l+1, r-1)

arr = [1,2,3,4,5]
# reverse_array(0, len(arr) - 1)
# print(arr)

# Fibonacci, multiple recursion calls
def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
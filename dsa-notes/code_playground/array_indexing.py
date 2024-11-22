## Find the First Prime Number in an Array
def findFirstPrime(arr=[4, 6, 8, 9, 10, 13, 15, 17]):

    def isPrime(num):
        if num <= 1:
            return False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False # Divisible by a number other than 1 and itself

        return True
    
    for num in arr:
        if isPrime(num):
            return num
    
    return None # Return null if no prime is found

# print(findFirstPrime())

### 2D array example
array_2d = [
    [1, 2, 3, 13],
    [4, 5, 6, 14],
    [7, 8, 9, 15],
    [10, 11, 12, 16]
]

## Traverse a Two-Dimensional Array
def traverse2dArray(arr):
    for row in arr:
        for column in row:
            print(column)

## Traverse the Main Diagonal of a Matrix

def diagonalTraverse2dArray(arr):

    counter = 0

    for row in arr:
        if counter < len(row):
            print(row[counter])
            counter += 1
            continue
        else:
            break

# diagonalTraverse2dArray(array_2d)

## Traverse the Perimeter of a Matrix

def traversePerimeter(matrix):
    # Handle edge cases
    if not matrix or not matrix[0]:
        return  # Empty matrix
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Top row (left to right)
    for col in range(cols):
        print(matrix[0][col])
    
    # Right column (top to bottom, excluding the first row)
    for row in range(1, rows):
        print(matrix[row][cols - 1])
    
    # Bottom row (right to left, if there are multiple rows)
    if rows > 1:
        for col in range(cols - 2, -1, -1):
            print(matrix[rows - 1][col])
    
    # Left column (bottom to top, excluding the first and last rows)
    if cols > 1:
        for row in range(rows - 2, 0, -1):
            print(matrix[row][0])

# traversePerimeter(array_2d)

def traverseSprial(arr):
    if not arr or not arr[0]:
        return []
    
    # define boundaries

    top, bottom = 0, len(arr) - 1
    left, right = 0, len(arr[0]) - 1

    result = []

    # Loop until boundraies overlap

    while top <= bottom and left <= right:

        # traverse left to right on the top row
        for col in range(left, right + 1):
            result.append(arr[top][col])
        top += 1 # move the top boundary down

        # traverse from top to bottom on the right column
        for row in range(top, bottom + 1):
            result.append(arr[row][right])
        right -= 1 # move right boundary to the left

        # traverse from right to left on the bottom row
        if top <= bottom: # Check to ensure we haven't passed the bottom boundary
            for col in range(right, left - 1, -1):
                result.append(arr[bottom][col])
            bottom -= 1 # Move the bottom boundary up
        
        # traverse from bottom to top on the left column
        if right <= left: # Check to ensure we haven't passed the left boundary
            for row in range(bottom, top - 1, -1):
                result.append(arr[row][left])
            left += 1 # Move the left boundary right

    return result

print(traverseSprial(array_2d))

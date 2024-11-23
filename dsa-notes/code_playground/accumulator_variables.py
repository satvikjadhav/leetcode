array = [-1, -3, 1, 2, 3, 6, 9, 8, 7, 4, 5, 10, 14, 12, 11, 13, 16, 17, 19, 21, 18, 20]

## Calculate the Sum of an Array
def sumArray(arr):
    total = 0

    for num in arr:
        total += num

    return total

# print(sumArray(arr=array))

## Find the Minimum and Maximum Elements
def minMax(arr):

    small = float('inf')
    big = float('-inf')

    for num in arr:
        small = min(small, num)
        big = max(big, num)
    
    return small, big

# print(minMax(array))

## Find the Indices of the Min and Max Elements
def minMaxIndex(arr):

    small = float('inf')
    small_index = 0
    big = float('-inf')
    big_index = 0

    for i in range(len(arr)):
        small = min(small, arr[i])
        if arr[i] == small:
            small_index = i
        big = max(big, arr[i])
        if arr[i] == big:
            big_index = i
    
    return small_index, big_index

# print(minMaxIndex(array))

## Find the Two Smallest/Largest Elements Without Sorting
def twoSmallBig(arr):
    large = float('-inf')
    second_large = float('-inf')
    small = float('inf')
    second_small = float('inf')

    for num in arr:
        small = min(small, num)
        large = max(large, num)

        if second_large < num < large:
            second_large = num

        if second_small > num > small:
            second_small = num
    
    return small, second_small, large, second_large

# print(twoSmallBig(array))

## Count Occurrences of a Specific Element
def countOccurenceOfElement(arr, n):

    counter = 0

    for num in arr:
        if num == n:
            counter += 1

    return counter

# print(countOccurenceOfElement(array, 2))

## Count Occurrences of All Elements
def countOccurence(arr):

    dict_counter = {}

    for num in arr:
        if num not in dict_counter:
            dict_counter[num] = 1
        else:
            dict_counter[num] += 1
    
    return dict_counter

# print(countOccurence(array))

## Find the Two Most Frequent Elements
arr = [1, 3, 3, 5, 1, 3, 7, 7, 7, 5, 1, 1]
def twoMostFrequent(arr):
    counter = {}

    for num in arr:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    most_frequent = [None, None]
    frequency = [0, 0]

    for elem, freq in counter.items():
        if freq > frequency[0]: # If the current frequency is higher than the first
            most_frequent[1] = most_frequent[0]
            frequency[1] = frequency[0]
            most_frequent[0] = elem
            frequency[0] = freq
        elif freq > frequency[1]: # If it's higher than the second but not the first
            most_frequent[1] = elem
            frequency[1] = freq
    print(counter)
    return most_frequent, frequency

# print(twoMostFrequent(arr))

## Compute Prefix Sums
def prefixSum(arr):

    res = []
    sum = 0
    for num in arr:
        sum += num
        res.append(sum)

    return res

# print(prefixSum(array))

## Find the Sum of Elements in a Given Range
def sumRange(arr, start, end):

    if start < 0 or end > len(arr) - 1:
        return
    
    sum = 0

    for i in range(start, end+1):
        sum += arr[i]
    
    return sum
        
# print(sumRange(array, 2,5))

## Efficient Range Sum Queries Using Prefix Sums

def rangeSumQueries(arr, start, end):

    sum = 0
    prefix_arr = []
    for num in arr:
        sum += num
        prefix_arr.append(sum)
    
    return prefix_arr[end] - prefix_arr[start-1] 

print(rangeSumQueries(array, 2, 5))


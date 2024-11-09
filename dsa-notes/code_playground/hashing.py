from collections import Counter

def find_unique(dictionary: dict):
    # Count the frequency of each number in the array
    arr = dictionary.values()
    frequency = Counter(arr)
    
    # Return the numbers that appear exactly once
    return [num for num, count in frequency.items() if count == 1]

# Example usage
dictionary = {"key1": 1, "key2": 1, "key3": 7, "key4": 3, "key5": 4, "key6": 7}
unique_values = find_unique(dictionary)
print(f"The unique values are: {unique_values}")

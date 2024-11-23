## Count of Subarrays with Sum K

arr = [3, 4, 7, 2, -3, 1, 4, 2]

def countSubarraysWithSumK(arr, k):
    prefix_sum = 0
    sum_count = {0: 1} # Initialize with 0 sum seen once
    count = 0
    prefix_arr = []

    for num in arr:
        prefix_sum += num
        prefix_arr.append(prefix_sum)
        # If we've seen (prefix_sum - k), add those occurrences
        if (prefix_sum - k) in sum_count:
            count += sum_count[prefix_sum - k]
        # Update count of current prefix_sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count

print(countSubarraysWithSumK(arr, 7))        
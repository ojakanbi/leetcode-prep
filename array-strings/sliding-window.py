"""
Sliding Window Approach for Fixed-Length Subarrays

This function extracts all contiguous subarrays (windows) of a given length from an input array.
The sliding window technique is efficient for problems where you're required to work with 
contiguous elements in an array, such as:

- Finding the maximum or minimum sum of subarrays of size 'k'
- Detecting patterns or properties within subarrays of fixed size
- Moving windows over a sequence for optimization

Related LeetCode problems:
1. Maximum Sum Subarray of Size K: https://leetcode.com/problems/maximum-average-subarray-i/
2. Longest Subarray with Sum Less than K: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
3. Minimum Size Subarray Sum: https://leetcode.com/problems/minimum-size-subarray-sum/

The function is a simple implementation that prints all subarrays of size 'length' from the input list 'arr'.
"""

def subArray(arr, lenght):
    storage = []
    
    # Loop to extract subarrays from valid starting points
    for startingIndex in range(len(arr) - length + 1):
        storage.append(arr[startingIndex:startingIndex + length])

    return storage

    
arr = [1,2,3,4,5,6]
length = 3
print("Sliding Window Approach:\n" ,subArray(arr,length))
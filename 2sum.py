# Hash map approach for the most efficient solution to the 2-sum problem
# My Leetcode submission: https://leetcode.com/problems/two-sum/submissions/1376754893

def twoSum(nums, target):
    # Create a hash map to store the indices of the numbers
    prevMap = {}
    
    # Iterate through the list of numbers
    for i, n in enumerate(nums):
        diff = target - n  # Calculate the difference needed to reach the target
        if diff in prevMap:  # Check if the difference is already in the hash map
            return [prevMap[diff], i]  # If found, return the indices of the two numbers
        prevMap[n] = i  # Store the index of the current number in the hash map
    return
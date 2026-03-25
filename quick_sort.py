# Here’s the code for quicksort:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
print(quick_sort([3, 6, 8, 10, 1, 2, 1]))   

# In this implementation, the quick_sort function takes an array as input. If the array has one or zero elements, it is already sorted, so we return it. Otherwise, we select the first element as the pivot and partition the remaining elements into two sub-arrays: one with elements less than or equal to the pivot and another with elements greater than the pivot. We then recursively call quick_sort on both sub-arrays and concatenate the results with the pivot in between to get the sorted array.


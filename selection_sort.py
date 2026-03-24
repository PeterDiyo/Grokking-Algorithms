# Sort an array from smallest to largest. Let’s write a function
# to find the smallest element in an array:

def findSmallest(arr):
    smallest = arr[0] #A
    smallest_index = 0 #B
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#A Stores the smallest value
#B Stores the index of the smallest value


# We can use this function to implement selection sort:
def selectionSort(arr):
    newArr = []
    copiedArr = list(arr) # copy array before mutating
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
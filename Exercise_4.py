# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
  # Finding the mid of the array
    mid = len(arr) // 2
  # Dividing the array elements into 2 halves
    L = arr[:mid]
    R = arr[mid:]
  # Sorting the first half
    mergeSort(L)
  # Sorting the second half
    mergeSort(R)
  # Merging the sorted halves
    i = j = k = 0
  # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
        k += 1

  # Check for any remaining elements
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
  
# Code to print the list 
def printList(arr): 
  for i in arr:
        print(i, end=" ")
  print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

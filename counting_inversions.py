def merge_and_count_significant(arr, temp_arr, left, mid, right):
    """
    Merges two sorted subarrays and counts significant inversions.
    A significant inversion is when arr[i] > 2*arr[j] where i < j.
    """
    # Count significant inversions before merging
    inv_count = 0
    j = mid + 1
    
    # For each element in left subarray, count elements in right subarray
    # that would form a significant inversion
    for i in range(left, mid + 1):
        # Find elements where arr[i] > 2*arr[j]
        while j <= right and arr[i] > 2 * arr[j]:
            j += 1
        # All elements from mid+1 to j-1 form significant inversions with arr[i]
        inv_count += (j - (mid + 1))
    
    # Reset indices for merging
    i = left
    j = mid + 1
    k = left
    
    # Regular merge operation
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:  
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1

    # Copy remaining elements of left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements of right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy sorted temp array back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count_significant(arr, temp_arr, left, right):
    """
    Uses merge sort to count significant inversions in the array.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Count inversions in left and right subarrays
        inv_count += merge_sort_and_count_significant(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count_significant(arr, temp_arr, mid + 1, right)
        
        # Count cross inversions and merge
        inv_count += merge_and_count_significant(arr, temp_arr, left, mid, right)

    return inv_count

def count_significant_inversions(arr):
    """
    Counts the number of significant inversions in an array.
    A significant inversion is a pair (i,j) where i < j and arr[i] > 2*arr[j].
    """
    temp_arr = arr.copy()
    return merge_sort_and_count_significant(arr, temp_arr, 0, len(arr) - 1)


# Test cases
def test_significant_inversions():

    arr1 = [5, 2, 6, 1]
    print(f"Array: {arr1}, Significant inversions: {count_significant_inversions(arr1)}")
    

    arr2 = [8, 4, 2, 1]
    print(f"Array: {arr2}, Significant inversions: {count_significant_inversions(arr2)}")

# Run the test function
if __name__ == "__main__":
    test_significant_inversions()
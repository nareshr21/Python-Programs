
def binary_search_element(arr, target):
    "Perform a binary search to find the target in a sorted array."

    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Return -1 if the target is not found




arr = [10, 20, 30, 40, 50]
print("Sorted array:", arr)
target = int(input("Enter the number to search: "))
result = binary_search_element(arr, target)
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found.")


def linear_search_program(arr, target):
    "Perform a linear search to find the target in the array."
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

arr = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))
result = linear_search_program(arr, target)
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found.")


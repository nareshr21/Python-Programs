
def array_sum(arr, index):
    "Calculate the sum of array elements using recursion."

    
    if index == len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)




arr = list(map(int, input("Enter the array elements separated by space: ").split()))
result = array_sum(arr, 0)
print(f"The sum of the array elements is {result}.")

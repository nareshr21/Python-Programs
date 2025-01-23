def find_target_element_index(arr,target):
    
    #Finding the target element index in  an array by taking input from user 


    n=len(arr)
    
    for i in range(n):
        if arr[i]==target: #Returning the index of target element
            return i

    return -1 #Returning -1 if target element is not found

arr=[10, 20, 30, 40, 50]
target=int(input("Enter the target element:"))


result=find_target_element_index(arr,target)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element is not found")

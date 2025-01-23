def maximum_element(arr):

    #Returning the maximum element in an array using iterative method
    
    max_element=arr[0] # intializing first element as max element

    n=len(arr)
    for i in range(n):
        if arr[i]>max_element: #checking  if the current element is greater element 
            max_element=arr[i] #reassinging the current element as max element
    return max_element

arr=list(map(int,input("Input elements in an array:").split()))

result=maximum_element(arr)
print("Maximum element is :",result)

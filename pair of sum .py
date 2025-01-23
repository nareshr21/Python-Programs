def pair_of_sum(arr,target):

    #Returning the pair that sum up to target using the two pointer method
    
    n=len(arr)
    found=False
    left=0  
    right=n-1

    while left<right: # this loop runs until left and right pointer meets
        current_sum=arr[left]+arr[right]

        if current_sum==target: #checking current sum equals to the target
            found=True
            return (arr[left],arr[right])#returning the pair
        
        elif current_sum<target: 
            left+=1  #if the current sum is less than target increments the left  pointer
        else:  
            right-=1  #if the current sum is greater than target increments the right pointer

    if found==False:
        print("No combination of sum")
            

arr=list(map(int,input("Input elements in an array:").split()))
target=int(input("Enter the target:"))

result=pair_of_sum(arr,target)

print("Pair of sum is :",result)




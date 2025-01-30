def find_an_element_appears_one(arr):
    #returning element that appears one
    
    n=len(arr)
    for num in arr:
        count=arr.count(num)#counting frequency of each element
        if count==1: # if count is 1
            return num #printing that number

    return None


arr=list(map(int,input("Enter elements in an array:").split()))
print(find_an_element_appears_one(arr))

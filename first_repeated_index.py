def first_repeated_index(arr):

    #Returning the first repeated index

    n=len(arr)
    unique=set()#initializing the set data structure for finding repeated element

    for i in range(n):
        if arr[i] in unique:# if current element is already present in unique set
            return i #return its index
        else:
            unique.add(arr[i])# if current element is not in unique add that element into set data structure
    return -1 #there is no repeated element return -1



arr=[1,2,1,1,3,4,5]
result=first_repeated_index(arr)

if result!=-1:
    print("First repeated element occuring at index:",result)
else:
    print("No repeated element")

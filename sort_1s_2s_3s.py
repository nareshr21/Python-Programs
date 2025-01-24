def sort_0s_1s_2s(arr):
    # Soring 0s and 1s and 2s without using sort() method
    
    count_0 = arr.count(0) #counting 0
    count_1 = arr.count(1) #counting 1
    count_2 = arr.count(2) #counting 2

    index=0

    for _ in range(count_0):#placing the 0s at the front using index
        arr[index]=0
        index+=1

    for _ in range(count_1):#placing the 1s after 0s using index
        arr[index]=1
        index+=1

    for _ in range(count_2):#placing the 2s after 1s using index
        arr[index]=2
        index+=1

    return arr # after modifying the original array return final array


arr=list(map(int,input("Enter elements in an array:").split()))
print("Sorted array:",sort_0s_1s_2s(arr))

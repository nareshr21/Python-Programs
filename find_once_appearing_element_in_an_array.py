def find_single_brute_force(arr):

    #finding an element that appears once where every other element appears twice
    
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1#incrementing count if element is present in both loops are equal
        if count==1:#if count is 1 returning that element
            return arr[i]

    return None

arr = list(map(int,input("Enter elements in an array:").split()))
print("Element occurring once is:", find_single_brute_force(arr))

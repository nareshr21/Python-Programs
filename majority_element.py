def find_majority_element(arr):
    #Returning the majority element in an array using the brute force method"

    #Majority element is element appears n//2 times in an array
    
    n = len(arr)
    majority_count = n // 2

    for i in range(n):
        count = 0    #initializing count as 0
        for j in range(n):
            if arr[i] == arr[j]: #if current element of j is equal to the current element of i
                count += 1 #increment count

        if count > majority_count:
            return arr[i]

    return "No Majority Element"


arr=list(map(int,input("Enter elements in an array:").split()))
print("Majority element is :",find_majority_element(arr))

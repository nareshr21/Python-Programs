def frequency_of_element(arr):

    #Returning the frequency of each element in an array using dictionary
    
    counts={}

    for num in arr:
        if num in counts:
            counts[num]+=1 #incrementing the count if element is already present in dictionary
        else:
            counts[num]=1 #assinging 1 if element is new to dictionary
            

    return counts


arr=list(map(int,input("input elements in an array:").split()))
result=frequency_of_element(arr)
print("Frequency of each element  in an array:",result)



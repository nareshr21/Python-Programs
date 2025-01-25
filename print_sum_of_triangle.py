def print_triangle(arr):
    #print_sum_of_triangle
    
    if len(arr)<1:#when the length of the array reaches less than 1 its return it
        return


    next_level=[arr[i]+arr[i+1] for i in range(len(arr)-1)] #adding the current element with next element 

    print_triangle(next_level)#calling recursively for sum of elements in an array in an triangle wave form

    print(arr)

arr =list(map(int,input("Enter elements in an array:").split()))
print_triangle(arr)

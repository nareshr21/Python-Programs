def perfect_number(n):

    #returning a number it is a perfect number
    #perfect number is sum of factors of that number except itself is equal to the original number
    result=[]
    for i in range(1,n):
        if n%i==0:#generating all the factors from 1 to n
            result.append(i)

    return result


n=int(input("Enter the number:"))
result=perfect_number(n)
if sum(result)==n:#checking if a sum of factors is equal to the number
    print("The given number is perfect number")
else:
    print("The given number is not a perfect number")
    

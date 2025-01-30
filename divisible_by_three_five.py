def divisible_by_three_five(n):

    #returning the string array where index is divisible by 3 or 5 or both printing strings
    
    result=[]

    
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result

n=int(input())
print(divisible_by_three_five(n))

def string_balanced(s1,s2):
    #returning the strings are balanced by true or false
    
    flag = True #initializing the flag as true
    for char in s1: #iterating all the characters in s1
        if char in s2:  #iterating all the characters in s2
            continue
        else:
            flag = False 

    return flag

s1 = "Yn"
s2 = "PYnative"
print("s1 and s2 are balanced :",string_balanced(s1,s2)
)

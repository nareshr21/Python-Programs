def phrase_palindrome(s):

    #returning the string is palindrome or not
    #converting uppercase to lowercase and remove all non-aplhanumeric characters
    
    s=s.lower()
    new_string="".join(filter(lambda x:x.isalnum(),s))#using lambda expression is one of the way to remove non-aplhanumberic characters without looping

    if new_string==new_string[::-1]:
        return "The given string is palindrome"
    else:
        return "The given string is not a palindrome"
        
    


s=input("Enter the string:")
print(phrase_palindrome(s))

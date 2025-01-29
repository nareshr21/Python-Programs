import string #importing string for using punctuation method which is available module of str.maketrans and str.translate

def remove_punctuation(str1):
    #Returning the string by removing punctuation characters present in a given string
    
    new_str=str1.translate(str.maketrans("","",string.punctuation))

    return new_str

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)
print(remove_punctuation(str1))



def find_all_occurences_of_substring(str1,sub_string):

    #Returning the count of occurences of substring present in a given string
    
    temp_str=str1.lower() #changing uppercase to lowercase

    count=temp_str.count(sub_string.lower()) #counting the substring occurences using count() method

    return count


str1="Welcome to USA. usa awesome, isn't it?"

sub_string="USA"

print("USA count is :",find_all_occurences_of_substring(str1,sub_string))

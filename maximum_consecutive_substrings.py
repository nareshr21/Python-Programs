def  maximum_consecutive_substrings(string,sub_str):

    #returning maximum consecutive substrings present in the string

    max_count=0#for tracking count of substring
    max_sub=""#for substring identification

    words=string.split()

    for word in words:
        count=word.count(sub_str)

        if count>max_count:#if count if greater than max count then there is substring which occuring more than once
            max_count=count
            max_sub=sub_str*max_count

    return max_sub,max_count


            

string='geeksgeeks are geeks for all geeksgeeksgeeks'

sub_str="geeks"

print("Original string:", string)
max_sub,max_count=maximum_consecutive_substrings(string,sub_str)

print("Maximum run of substring:", max_sub)
print("Maximum count :",max_count)

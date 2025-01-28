def count_distinct_substrings(s):

    #count distinct substrings

    substrings=set()#for counting distinct we are using set data structure

    for i in range(len(s)):
        for j in range(i,len(s)):
            substrings.add(s[i:j +1])#adding to the set 

    return len(substrings)#returning length og the substrings which means count

string=input("Enter the string:")
print(count_distinct_substrings(string))


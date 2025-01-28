def sort_a_list_alphabetically_in_dictionary(num):

    #sort  a list alphabetically in dictionary

    sorted_dict={x: sorted(y) for x,y in num.items()} #iterating  a dictionary for keys and values we are using two variables x and y 

    return sorted_dict

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
print(sort_a_list_alphabetically_in_dictionary(num))

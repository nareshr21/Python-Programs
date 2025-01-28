def remove_keys_with_substring_values(test_dict,sub_list):
    
    #returning by removing keys with substring values present

    for key,value in list(test_dict.items()):   #Accessing the items in the dictionary
        for sub in sub_list:   #Acessing the values in the list
            if sub in value:   #If the value is prsent in dictionary remove it by using pop method
                test_dict.pop(key)



test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
sub_list = ['love', 'good']
print(remove_keys_with_substring_values(test_dict,sub_list))



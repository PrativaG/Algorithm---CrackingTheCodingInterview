def permutationCheck(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_dict = {}
    str2_dict = {}

    for i in range(len(str1)):
        if str1[i] not in str1_dict:
            str1_dict[str1[i]] = 1
        elif str1[i] in str1_dict:
            str1_dict[str1[i]] +=1

        if str2[i] not in str2_dict:
            str2_dict[str2[i]] = 1
        elif str2[i] in str2_dict:
            str2_dict[str2[i]] +=1
    
    print(str1_dict)
    print(str2_dict)
    if str1_dict == str2_dict:
        return True
    
    return False

print(permutationCheck("abdjkce", "edcba"))
def uniqueCharacter(str):
    for i in range(len(str)-1):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return False
            
    return True

print(uniqueCharacter("abcde"))
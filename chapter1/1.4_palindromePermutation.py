def palindromePermutation(anyStr):
    str = anyStr.lower()
    palinCheck = {}
    countOdd = 0

    for i in range(len(str)):
        if str[i] not in palinCheck and str[i] != " ":
            palinCheck[str[i]] = 1
        elif str[i] in palinCheck:
            palinCheck[str[i]] += 1
        
    for k, v in palinCheck.items():
        if v % 2 == 1:
            countOdd += 1
        
        if countOdd > 1:
            return False
        
    return True

print(palindromePermutation("taco caT"))
print(palindromePermutation("tacodcat"))
print(palindromePermutation("nichousa"))
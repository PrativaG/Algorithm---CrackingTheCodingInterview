
def oneAway(str1, str2):
    lenDiff =  len(str1) - len(str2)

    if abs(lenDiff) > 1:
        return False
    
    # charCheck = {}

    # for i in range(len(str1)):
    #     if str1[i] not in charCheck:
    #         charCheck[str1[i]] = 1 
    #     else:
    #         charCheck[str1[i]] += 1
    
    # for j in range(len(str2)):
    #     if str2[j] not in charCheck:
    #         charCheck[str2[j]] = 1
    #     else:
    #         charCheck[str2[j]] += 1

    # countEdits = 0
    # for v in charCheck.values():
    #     if v % 2 == 1:
    #         countEdits += 1
        
    #     if countEdits >= 3:
    #         return False
        
    # return True

    charCheck = []

    for i in range(len(str1)):
       charCheck.append(str1[i])
    
    for j in range(len(str2)):
        charCheck.append(str2[j])

    print(charCheck)

    countEdits = 0
    for i in range(len(charCheck)):
        if v % 2 == 1:
            countEdits += 1
        
        if countEdits >= 3:
            return False
        
    return True

print(oneAway("pale", "pie"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))

print(oneAway("pat", "apt"))



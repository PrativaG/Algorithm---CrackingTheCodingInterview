# def stringCompression(mystr):
#     countLetters = {}
#     compressedStr = ""

#     for i in range(len(mystr)):
#         if mystr[i] not in countLetters:
#             countLetters[mystr[i]] = 1
        
#         else:
#             countLetters[mystr[i]] += 1
    
#     for k, v in countLetters.items():
#         compressedStr += k
#         compressedStr += str(v)  
    
#     if len(compressedStr) >= len(mystr):
#         return mystr
    
#     return compressedStr

def stringCompression(myStr):
    count = 1
    newStr = myStr[0]

    for i in range(1, len(myStr)):
        if myStr[i] == myStr[i-1]:
            count += 1
        else:
            newStr += str(count)
            count = 1
            newStr += myStr[i]

    newStr += str(count)

    if len(myStr) < len(newStr):
        return myStr
    
    return newStr

print(stringCompression("aabbccccdddee"))
print(stringCompression("abcdekj"))

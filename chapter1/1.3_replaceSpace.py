# def replaceSpace(str):
#     newStr = ""
#     for i in range(len(str)):
        
#         if str[i] == " ":
#             newStr += "%20"
#         else:
#             newStr += str[i]
    
#     return newStr

# OR

def replaceSpace(str):
    replacedStr = str.replace(" ", "%20")
    return replacedStr

print(replaceSpace("Hy My Name is Prativa"))
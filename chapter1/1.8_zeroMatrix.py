def zeroMatrix(arr):
    rowWithZero = {}
    columnWithZero = {}

    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if arr[i][j] == 0:
                rowWithZero[i] = True
                columnWithZero[j] = True
        
    for m in range(len(arr)):
        for n in range(len(arr[m])):
            if m in rowWithZero:
                arr[m][n] =0
            elif n in columnWithZero:
                arr[m][n] = 0
    
    return arr

mn = [
        [20, 10, 0, 3, 2],
        [5, 6, 3, 1, 0],
        [0, 5, 9, 2, 0],
        [37, 91, 82, 33, 5]
        ]
print(zeroMatrix(mn))
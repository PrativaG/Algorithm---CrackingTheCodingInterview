# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

# [ HINTS ]
#51. 1.7 Try thinking about it layer by layer. Can you rotate a specific layer? 
#100. 1.7 Rotating a specific layer would just mean swapping the values in four arrays. If you were asked to swap the values in two arrays, could you do this? Can you then extend it to four arrays? 


# [
#     [1, 2, 3],  2== mat[0][1]
#     [4, 5, 6],  6== mat[1][2]
#     [7, 8, 9]
# ];
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ];

# [ NOT WORKING, NEED TO FIX IT ]

def rotateMatrix(mat):

    count = 0
    for i in range(0, len(mat) - 1):
        for j in range(i, len(mat[i])-1):
            # 1, 3, 9, 7 => 7, 1, 3, 9
            # 2, 6, 8, 4 => 4, 2, 6, 8
            #2 j=1 -1-1 -2 3-2 =1
            # 0,1 1,2 2,1 1,0 => 1,0 0,1 1,2 0,1
            mat[ i ][ j ], mat[ i+j ][ len(mat) - 1], mat[len(mat) - 1][ len(mat) - 1-j], mat[len(mat) - 1-j][i] =   mat[len(mat) - 1-j][i],  mat[ i ][ j ], mat[ i+j ][ len(mat) - 1],  mat[len(mat) - 1][ len(mat) - 1-j]
            count += 1
            print(count)
    return mat


arr = [
   [1, 2, 3], 
   [4, 5, 6],  
    [7, 8, 9]
]

arr2 = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [13,14,15,16],
]
   


print(rotateMatrix(arr2))











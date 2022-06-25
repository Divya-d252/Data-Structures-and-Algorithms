# Problem Statement

# https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1

# Given an ‘N’ x ‘M’ integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. In particular, your task is to 
# modify it in such a way that if a cell has a value 0 (matrix[i][j] == 0), then all the cells of the ith row and jth column should be changed to 0.
# You must do it in place.

# For Example:
# If the given grid is this:
# [7, 19, 3]
# [4, 21, 0]

# Then the modified grid will be:
# [7, 19, 0]
# [0, 0,  0]

1. Time Complexity - O(N*M)*O(N+M) Space Complexity - O(1)

Approach - Brute Force, For every value in the matrix, if element is 0 then traversing through the particular row and column and setting it as -1, at the 
end traversing through whole matrix, setting all the -1s to 0s

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for m in range(len(matrix[0])):
                    if matrix[i][m] != 0:
                        matrix[i][m] = -1
                for k in range(0,len(matrix)):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    pass
    
2.Time Complexity - 2*O(N*M) Space Complexity - O(M+N)

Approach - Saving Time, assuming a row and column matrix and for every matrix(i)(j)=0 putting the corresponding row(i) and column(j) to 0 and then tranversing 
through matrix and setting element to 0 if the corresponding row(i) or column(j) = 0.

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row = [-1 for i in range(len(matrix))]
    col = [-1 for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 0 or col[j] == 0:
                matrix[i][j] = 0
    pass
    
3. Time Complexity - 2*O(N*M) Space Complexity - O(1)

Approach - Saving space along with time - Instead taking 2 arrays consuming extra space, we take the first row and first column as the row and column 
array as we did for the previous approach,

1. for the first row, we maintain a flag which is initially true, if any of the elements of the first row is 0, we set the flag to False
2. from the second row, for every matrix(i)(j) is 0 the corresponding matrix(i)(0) = 0 and matrix(0)(j) = 0
3. Then traversing backwards for every matrix(i)(0) or matrix(0)(j) = 0 we set the matrix(i)(j) = 0 (expect for the first row)(traversing from backwards 
   to ensure the first row do not get manipulated first as the other rows are dependent on it - raising conflicts)
4. For the first row, we check if the flag is False then all the values of the first row are set to 0


why we took a flag for the first row ??

1. Manipulating the first row or first column based on matrix element values can lead to certain conflicts which need to be taken care of.
2. For ex: consider if matrix(3)(0) = 0 then normally we would do matrix(0)(0) = 0, then while traversing backwards say for any matrix(0)(j) where the 
   value depends on matrix(0)(0), matrix(0)(j) will be set to 0 even though the corresponding row or column does not having any 0's causing an anomaly.
3. The flag is to ensure that for the first row, we make the desicion based on the flag thereby not causing any anomaly.


def setZeros(matrix: List[List[int]]) -> None:
    flag = True
    
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            flag = False
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
            
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,0,-1):
            if matrix[i][0] == 0 or matrix[0][j] == 0: 
                matrix[i][j] = 0
        if flag == False:
            matrix[i][0] = 0
                

IMP 

# https://www.codingninjas.com/codestudio/problems/1089580?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

# You are given an integer N. Your task is to return a 2-D ArrayList containing the pascal’s triangle till the row N.
# A Pascal's triangle is a triangular array constructed by summing adjacent elements in preceding rows. Pascal's triangle contains the values of the binomial coefficient. For example in the figure below.

# For example, given integer N= 4 then you have to print.
# 1  
# 1 1 
# 1 2 1 
# 1 3 3 1

# Here for the third row, you will see that the second element is the summation of the above two-row elements i.e. 2=1+1, and similarly for row three 3 = 1+2 and 3 = 1+2.

1. To Compute every row of the pascal's triangle 

TC - O(N^2) and SC - O(N^2) - Brute force basic approach:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r1 = [1]
        r2 = [1,1]
        r = [r1,r2]
        for i in range(2,numRows):
            r3 = [1]
            for j in range(len(r2)-1):
                r3.append(r2[j]+r2[j+1])
            r3.append(1)
            r.append(r3)
            r2 = r3

        return r[:numRows]

def printPascal(n:int):
    r = [[] for i in range(n)]
    for i in range(0,n):
        r[i]=[1]*(i+1)
        for j in range(1,i):
            r[i][j] = r[i-1][j-1] + r[i-1][j]      
    return r[:n] 
    pass
  
2. To Compute nth row of the pascal's triangle

TC - O(N) and SC - O(N)

For computing any nth row, (n-1)C0, (n-1)C1, -- (n-1)C(n-1) i.e, for 4th row [3C0, 3C1, 3C2, 3C3] = [1, 3, 3, 1]
But it takes O(N2) complexity, O(N) for nCr formula and O(N) for computing the particular row. Let's look at the better approach of this

[1,3,3,1] => [3C0, 3C1, 3C2, 3C3] => [1, 1*(3/1), 1*(3/1)*(2/2), 1*(3/1)*(2/2)*(1/3)]
i.e, to compute every next element we multiply the previous element value with (n-i) and divide with i where i starting from 1 to n

def printPascal(n:int):
    r1 = 1
    res = [r1]
    for i in range(1,n):
        r1 = r1*(n-i)
        r1 = r1//i
        res.append(r1)
    print(res)
    pass
  
  
  3. To compute rth row cth column of the pascal's triangle
  
  TC - O(N) and SC - O(1)
  
  Ex: 8th row 3rd column the formula for computing is (n-1)C(r-1) as below:
  
  def printPascal(n:int):
    row = 7
    column = 2
    min1= min(column,row-column)
    res = 1
    for i in range(min1):
        res*=(row-i)
        res//=(i+1)
    print(res)

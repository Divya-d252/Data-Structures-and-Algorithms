# https://www.codingninjas.com/codestudio/problems/630526?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

# Problem Statement

# You are given an array (ARR) of length N, consisting of integers. You have to find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.
# A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning, and 0 or more integers from the end of an array.
# Note :
# The sum of an empty subarray is 0.

# Constraints :
# 1 <= N <= 10^6
# -10^6 <= A[i] <= 10^6

# where N is the length of the array.
# A[i] represents the numbers present in the array.

# Time limit: 1sec
# Sample Input 1 :
# 9
# 1 2 7 -4 3 2 -10 9 1
# Sample Output 1 :
# 11

1. O(N^3) Time Complexity

def maxSubarraySum(arr, n):    
    max1=arr[0]
    for i in range(0,n):
        for j in range(i,n):
            sum1=0
            for k in range(i,j+1):
                sum1+=arr[k]
            if sum1>=max1:
                max1=sum1
    return max(0,max1)
  
2. O(N^2) Time Complexity  

def maxSubarraySum(arr, n):    
    max1=arr[0]
    for i in range(0,n):
        sum1=0
        for j in range(i,n):
            sum1+=arr[j]
            if sum1>=max1:
                max1=sum1
    return max(0,max1)
  
3. O(N) Time Complexity

def maxSubArray(self, arr: List[int]) -> int:
    max1=arr[0]
    sum1=0
    for i in range(0,len(arr)):
        sum1+=arr[i]
        if sum1>max1:
            max1=sum1
        if sum1<0:
            sum1=0    
    return max1

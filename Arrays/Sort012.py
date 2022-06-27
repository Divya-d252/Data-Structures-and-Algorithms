# https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

1. Merge Sort - O(NlogN) complexity and O(N) Space Complexity

class Solution:
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Solution.mergeSort(L)
            Solution.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    def sortColors(self, nums: List[int]) -> None:
        Solution.mergeSort(nums)

2. Counting Sort - 2*O(N) Time and O(1) Space

def sortColors(self, nums: List[int]) -> None:
    c1,c2,c3=0,0,0
    for i in nums:
        if i==0:
            c1+=1
        if i==1:
            c2+=1
        if i==2:
            c3+=1
    k=0
    for i in range(c1):
        nums[k]=0
        k+=1
    for i in range(c2):
        nums[k]=1
        k+=1
    for i in range(c3):
        nums[k]=2
        k+=1
        
3. O(N) Time and O(1) Space

# Approach:
# --> 3 pointers low,mid,high, low and mid at start and high at end
# --> Need to traverse while mid<=high
# --> All elements to the left of low are 0's, to the right of high are 2's and in between all are 1's
# --> To execute step 3:
#   1. whenever arr[mid] = 0 we swap arr[mid],arr[low] and increment both low and mid.
#   2. whenever arr[mid] = 1 we increment mid.
#   3. whenever arr[mid] = 2 we swap arr[mid],arr[high] and decrement high.

def sortColors(self, nums: List[int]) -> None:
    low=0
    mid=0
    high=len(nums)-1
    while(mid<=high):
        if(nums[mid]==0):
            temp=nums[mid]
            nums[mid]=nums[low]
            nums[low]=temp
            low+=1
            mid+=1
        elif(nums[mid]==1):
            mid+=1
        else:
            temp=nums[mid]
            nums[mid]=nums[high]
            nums[high]=temp
            high-=1
    return nums

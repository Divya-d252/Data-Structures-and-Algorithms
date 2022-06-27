# https://leetcode.com/problems/next-permutation/

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

My approach:
  
Coding Ninjas:
----------------
def nextPermutation(permutation, n):
    if permutation == sorted(permutation, reverse = True):
        permutation = sorted(permutation)
    else:
        i=len(permutation)-1
        while(permutation[i] < permutation[i-1]):
            i-=1
        temp = permutation[i-1]
        sorted1= sorted(permutation[i-1:])
        permutation[i-1] = sorted1[sorted1.index(temp)+1]
        permutation = permutation[:i]+sorted1[:sorted1.index(temp)+1]+sorted1[sorted1.index(temp)+2:]
    return permutation
  
LeetCode:
-----------------
def nextPermutation(self, permutation: List[int]) -> None:
      if permutation == sorted(permutation, reverse = True):
          reverse = permutation[::]
          for i in range(len(permutation)):
              permutation[i]= reverse[len(permutation)-i-1]
      else:
          i=len(permutation)-1
          while(permutation[i] <= permutation[i-1]):
              i-=1
          temp = permutation[i-1]
          sorted1=sorted(permutation[i-1:])
          for k in sorted1:
              if k > temp:
                  min2=k
                  break
          sorted2=[min2]

          m=-1
          for k in sorted1:
              if (k!=min2) :
                  sorted2.append(k)
              if (k==min2 and m==-1):
                  m=1
              elif (k==min2):
                  sorted2.append(k)
          xx = permutation[:i-1]+sorted2
          for i in range(len(xx)):
              permutation[i] = xx[i]
    
    
Optimized Approach:
-----------------------
O(N) time complexity and O(1) Space complexity

Consider --> [1 5 2 4 3]

1. From the back check where arr[i]>arr[i-1] (4>2). element1=2
2. From the back check where an element is greater than element1 from the step 1. element2=3
3. Swap both 1 and 2 --> [1 5 3 4 2]
4. Now from the ith position reverse all elements --> [1 5 3 2 4]

def nextPermutation(self, permutation: List[int]) -> None:
    if permutation == sorted(permutation, reverse = True):
        permutation.reverse()
    else:
        i=len(permutation)-1
        while(permutation[i] <= permutation[i-1]):
            i-=1
        temp = permutation[i-1]

        j=len(permutation)-1
        while(permutation[j] <= temp):
            j-=1

        swap=permutation[i-1]
        permutation[i-1]=permutation[j]
        permutation[j]=swap

        xx = permutation[:i]+list(reversed(permutation[i:]))
        for i in range(len(xx)):
            permutation[i] = xx[i]

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

1. Brute force - O(N^2) Time Complexity and O(1) Space Complexity - Simply traversing every possibility with i from i to n-1 and j to i+1 to n, and checking for the maximum
of prices[j]-prices[i] every time

def maximumProfit(prices):
    sum1=0
    for i in range(0,len(prices)-1):
        for j in range(i+1,len(prices)):
            if(prices[j]-prices[i]>sum1):
                sum1=prices[j]-prices[i]
    return sum1
 
2. Optimized Approach - O(N) Time Complexity and O(1) Space Complexity -

1. The approach is checking for the minimum element from the left of the array (keep track of)
2. And every time checking for the difference between the current element and min and keeping track of the maximum difference which is ultimately the best
time to buy and sell stocks.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=99999999
        ans=0
        max1=0
        for i in range(0,len(prices)):
            if prices[i]<min1:
                min1=prices[i]
            ans=prices[i]-min1
            if(ans>max1):
                max1=ans
        return max1

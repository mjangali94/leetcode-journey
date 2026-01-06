# Problem: Max Number of K-Sum Pairs
# LeetCode URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
# Description: You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
# challenge


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        ops = 0
        
        for num in nums:
            need = k - num
            
            if need in freq and freq[need] > 0:
                ops += 1
                freq[need] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
                
        return ops
 

# Problem: Move Zeroes
# LeetCode URL: https://leetcode.com/problems/move-zeroes/description/
# Description: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in nums:
            if i == 0:
                continue
            else:
                nums[j] = i
                j +=1
        for k in range(j,len(nums)):
            nums[k] = 0 
        
        

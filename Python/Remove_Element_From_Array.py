# Problem: Remove Element (equal to val) from array
# LeetCode URL: https://leetcode.com/problems/remove-element
# Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i =0 
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i

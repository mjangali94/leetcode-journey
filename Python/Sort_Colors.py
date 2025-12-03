# Problem: Sort Colors
# LeetCode https://leetcode.com/problems/sort-colors/description/
# Description: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Medium level



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return
        slow, fast = 0, 0
        while slow < len(nums) and nums[slow] == 0:
            slow +=1
        for fast in range(slow, len(nums)):
            if nums[fast] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
        while slow < len(nums) and nums[slow] == 1:
            slow +=1

        for fast in range(slow, len(nums)):
            if nums[fast] == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
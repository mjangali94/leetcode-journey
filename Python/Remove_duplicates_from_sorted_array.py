# Problem: remove duplicates from sorted array
# LeetCode URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Difficulty: Easy
# Description: Given an integer x, return true if x is a palindrome, and false otherwise.



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
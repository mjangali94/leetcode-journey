# Problem: single-number
# LeetCode URL: https://leetcode.com/problems/single-number/description/
# Difficulty: Easy
# Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                del dictionary[i]
            else:
                dictionary[i] = 1
            
        return next(iter(dictionary))
        


# Problem: single-number
# LeetCode URL: https://leetcode.com/problems/single-number/description/
# Description: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for a in nums:
            if not a in dictionary:
                dictionary[a] = 1
            else:
                dictionary[a] += 1
        
        for a, i in dictionary.items():
            if i == 1:
                return a
        return 0

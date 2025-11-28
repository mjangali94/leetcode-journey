# Problem: Contains Duplicate
# LeetCode URL: https://leetcode.com/problems/contains-duplicate/description/
# Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in nums:
            if not i in myMap:
                myMap[i] = 1
            else:
                return True
        return False

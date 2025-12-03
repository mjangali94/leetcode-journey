# Problem: Find First and Last Position of Element in Sorted Array
# LeetCode URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Description: Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# Medium level


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start,end = -1,-1
        for i,a in enumerate(nums):
            if a == target:
                start = i if start == -1 else start
                end = i
        return [start,end]
        
# Problem: Increasing Triplet Subsequence
# LeetCode URL: https://leetcode.com/problems/increasing-triplet-subsequence/description/
# Description: Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for i in nums:
            if i <= first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
        return False

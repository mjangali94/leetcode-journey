# Problem: Minimum Size Subarray Sum
# LeetCode URL: https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Description: Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Medium level

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        min_len = float('inf')
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >=target:
                min_len= min(min_len, right - left +1)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len
# Problem: Maximum Average Subarray I
# LeetCode URL: https://leetcode.com/problems/maximum-average-subarray-i/description/
# Description: You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -float('inf')
        left, right = 0, k-1
        cur_sum = 0
        for i in range(k):
            cur_sum +=nums[i]
        if cur_sum > max_avg:
            max_avg = cur_sum
        while right <len(nums)-1:
            cur_sum -= nums[left]
            left += 1
            right += 1
            cur_sum += nums[right]
            if cur_sum > max_avg:
                max_avg = cur_sum
        return max_avg / k
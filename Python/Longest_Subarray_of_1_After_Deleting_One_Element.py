# Problem: Longest Subarray of 1's After Deleting One Element
# LeetCode URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
# Description: Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_length = max(max_length, right-left+1)
        return max_length -1
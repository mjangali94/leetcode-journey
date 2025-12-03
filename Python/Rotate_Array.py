# Problem: Rotate Array
# LeetCode https://leetcode.com/problems/rotate-array/description/
# Description: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Medium level


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(a,b):
            while a < b:
                nums[a] , nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
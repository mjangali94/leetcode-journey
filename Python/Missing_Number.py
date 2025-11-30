# Problem: Missing Number
# LeetCode URL: https://leetcode.com/problems/missing-number/description/
# Description: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = (len(nums)* (len(nums) +1))//2
        for a in nums:
            n = n - a
        return n
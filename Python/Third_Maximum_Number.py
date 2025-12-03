# Problem: Third Maximum Number
# LeetCode URL: https://leetcode.com/problems/third-maximum-number/description/
# Description: Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) <3:
            return max(nums)
        count = 0
        maximum= 0
        while count<3:
            maximum = max(nums)
            nums.remove(maximum)
            count +=1
        return maximum

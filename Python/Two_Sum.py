# Problem: Two Sum
# LeetCode URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Description: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i ,j]

        dictionary = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dictionary:
                return [dictionary[complement], i]
            dictionary[num] = i
        
        return []
        
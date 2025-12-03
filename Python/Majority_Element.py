# Problem: Majority Element
# LeetCode https://leetcode.com/problems/majority-element/description/
# Description: Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n_2 = len(nums) // 2

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > n_2:
                return num
# Problem: Permutations
# LeetCode URL: https://leetcode.com/problems/permutations/description/
# Description: Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Medium level

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for a in nums:
            lst = self.permute([x for x in nums if x!=a])
            for b in lst:
                result.append([a]+b)

        return result
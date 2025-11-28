# Problem: Search Insert Position
# LeetCode URL: https://leetcode.com/problems/search-insert-position
# Description: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return i



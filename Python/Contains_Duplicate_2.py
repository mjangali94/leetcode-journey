# Problem: Contains Duplicate II
# LeetCode URL: https://leetcode.com/problems/contains-duplicate-ii/description/
# Description: Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}
        
        for i,a in enumerate(nums):
            if not a in myMap:
                myMap[a] = [i]
            elif a in myMap:
                for j in myMap[a]:
                    if abs(j - i) <= k:
                        return True
                myMap[a].append(i)
        return False

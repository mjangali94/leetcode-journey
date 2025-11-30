# Problem:  Intersection of Two Arrays II
# LeetCode URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# Description: Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# challenge



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1=Counter(nums1)
        counter_2=Counter(nums2)
        result = []

        for i in nums1:
            if i in nums2 and i not in result:
                result.extend([i] * min(counter_1[i] , counter_2[i]))

        return result
        
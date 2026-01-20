# Problem: Median of Two Sorted Arrays
# LeetCode URL: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Description: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            leftA = float('-inf') if i == 0 else nums1[i - 1]
            rightA = float('inf') if i == m else nums1[i]

            leftB = float('-inf') if j == 0 else nums2[j - 1]
            rightB = float('inf') if j == n else nums2[j]

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return max(leftA, leftB)

            elif leftA > rightB:
                high = i - 1
            else:
                low = i + 1
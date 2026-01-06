# Problem: Container With Most Water
# LeetCode URL: https://leetcode.com/problems/container-with-most-water/description/
# Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.



class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, h * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
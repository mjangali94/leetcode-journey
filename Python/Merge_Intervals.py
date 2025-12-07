# Problem: Merge Intervals
# LeetCode URL: https://leetcode.com/problems/merge-intervals/description/
# Description: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Medium level

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        left, right = intervals[0]

        for start, end in intervals[1:]:
            if start <= right:            
                right = max(right, end)   
            else:
                result.append([left, right])
                left, right = start, end  

        result.append([left, right])
        return result
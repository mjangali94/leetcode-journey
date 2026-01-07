# Problem: Unique Number of Occurrences
# LeetCode URL: https://leetcode.com/problems/unique-number-of-occurrences/description/
# Description: Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        counts = freq.values()
        return len(counts) == len(set(counts))




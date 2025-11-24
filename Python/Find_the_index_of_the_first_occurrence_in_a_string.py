# Problem: Find the Index of the First Occurrence in a String
# LeetCode URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
# Difficulty: Easy
# Description: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1
        
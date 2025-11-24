# Problem: length of last word
# LeetCode URL: https://leetcode.com/problems/length-of-last-word
# Difficulty: Easy
# Description: Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while "  " in s:
            s = s.replace("  "," ")
        if s[-1] == ' ':
            s= s[:-1]
        return len(s.split(" ")[-1])
        
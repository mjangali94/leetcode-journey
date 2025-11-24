# Problem: Longest Common Prefix
# LeetCode URL: https://leetcode.com/problems/longest-common-prefix
# Difficulty: Easy
# Description: Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix



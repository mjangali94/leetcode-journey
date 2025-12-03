# Problem: Is Subsequence
# LeetCode URL: https://leetcode.com/problems/is-subsequence/description/
# Description: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if ch in s and s[i]==ch:
                i +=1
        
        return i == len(s)
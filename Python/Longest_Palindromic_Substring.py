# Problem: Longest Palindromic Substring
# LeetCode URL: https://leetcode.com/problems/longest-palindromic-substring/description/
# Description: Given a string s, return the longest palindromic substring in s.


class Solution:
    def isPalindrome(self, s:str) -> bool:
        return s[:] == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        max_str = ""
        for left in range(len(s)):
            for right in range(left,len(s)):
                if self.isPalindrome(s[left:right+1]) and len(s[left:right+1]) >len(max_str):
                    max_str = s[left:right+1]
        return max_str




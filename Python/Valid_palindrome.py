# Problem: Valid Palindrome
# LeetCode URL: https://leetcode.com/problems/valid-palindrome/description/
# Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        for ch in s:
            ch = ch.lower()
            if ch not in "abcdefghijklmnopqrstuvwxyz0123456789":
                continue
            s_clean += ch

        return s_clean[::-1] == s_clean[:]
        

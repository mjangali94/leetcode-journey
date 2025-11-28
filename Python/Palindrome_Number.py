# Problem: Palindrome Number
# LeetCode URL: https://leetcode.com/problems/palindrome-number/
# Description: Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse :int = 0
        xcopy :int =  x
        while (x>0):
            reverse = reverse *10 + x%10
            x = x // 10
        if xcopy == reverse:
            return True
        return False
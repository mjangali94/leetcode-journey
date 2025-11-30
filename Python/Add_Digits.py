# Problem: Add Digits
# LeetCode URL: https://leetcode.com/problems/add-digits/description/
# Description: Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> int:
        while num //10 >0:
            a = num
            total = 0
            while a >0:
                total += a % 10
                a = a // 10
            num = total
        return num

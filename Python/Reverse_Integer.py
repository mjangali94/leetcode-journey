# Problem: Reverse Integer
# LeetCode URL: https://leetcode.com/problems/reverse-integer/description/
# Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Medium level

class Solution:
    def reverse(self, x: int) -> int:
        rvrsed=0
        is_negative = True if x<0 else False
        x *= -1 if x<0 else 1

        while x > 0:
            rvrsed +=x %10
            rvrsed *= 10 if x>=10 else 1
            x = x //10
        if rvrsed > 2147483647:
            return 0
        if is_negative:
            return rvrsed * -1
        else:
            return rvrsed
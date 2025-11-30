# Problem: Power of Two
# LeetCode URL: https://leetcode.com/problems/power-of-two/description/
# Description: Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n >1:
            if n%2==0:
                n = n /2
            elif n != 1:
                return False

        return n==1
            

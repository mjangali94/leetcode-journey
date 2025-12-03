# Problem: Pow(x, n)
# LeetCode https://leetcode.com/problems/powx-n/description/
# Description: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Medium level

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n//2)
        if n%2 ==0:
            return half*half
        else:
            return half * half * x
# Problem: Ugly Number
# LeetCode URL: https://leetcode.com/problems/ugly-number/description/
# Description: An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <1:
            return False
        while n > 1:
            if n % 2 == 0:
                n = n//2
                continue
            elif n%3 == 0:
                n = n//3
                continue
            elif n%5 ==0:
                n = n//5
                continue
            else:
                return False
        return True
        


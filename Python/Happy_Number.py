# Problem: Happy Number
# LeetCode URL: https://leetcode.com/problems/happy-number/description/
# Description: Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        
        happy = False
        n2 = n
        lst = []
        while not happy:    
            n3 = 0
            while n2>0:
                n3 += (n2%10)**2
                n2 = n2//10
            n2 = n3
            if n2 not in lst:
                lst.append(n2)
            else:
                return happy
            happy = n2 == 1
            if happy:
                return happy     


# Problem: Climbing Stairs
# LeetCode URL: https://leetcode.com/problems/climbing-stairs
# Difficulty: Easy
# Description: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def combinator(self, n: int, m: int) -> int:
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
    
    def climbStairs(self, n: int) -> int:
        total = 0
        n_2 = n // 2
        for i in range(0, n_2 + 1):   
            total += self.combinator(n - i, i)
        return total
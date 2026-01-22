# Problem: Min Cost Climbing Stairs
# LeetCode URL: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Description: You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# challenge

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = prev1 = 0

        for c in cost:
            curr = c + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
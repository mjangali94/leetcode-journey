# Problem: Minimum Path Sum
# LeetCode https://leetcode.com/problems/minimum-path-sum/description/
# Description: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Medium level
# challenge

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minSum = float('inf')
        m = len(grid)
        n = len(grid[0])
        
        def backtrack(a, b, total):
            nonlocal minSum
            
            if a == m-1 and b == n-1:
                minSum = min(minSum, total + grid[a][b])
                return
            
            if a < m-1:
                backtrack(a+1, b, total + grid[a][b])

            if b < n-1:
                backtrack(a, b+1, total + grid[a][b])

        
        backtrack(0,0,0)

        return minSum
        
# Problem: Unique Paths II
# LeetCode https://leetcode.com/problems/unique-paths-ii/description/
# Description: You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
# Medium level

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        counter = 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        def backtrack(a,b):

            nonlocal counter
            nonlocal m
            nonlocal n
            nonlocal obstacleGrid

            if a == m-1 and b == n-1:
                counter +=1
                return
            
            if a < m-1:
                if obstacleGrid[a+1][b] != 1:
                    backtrack(a+1,b)

            
            if b < n-1:
                if obstacleGrid[a][b+1] != 1:
                    backtrack(a,b+1)
        backtrack(0,0)
        return counter
                    
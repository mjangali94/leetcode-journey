# Problem: Equal Row and Column Pairs
# LeetCode URL: https://leetcode.com/problems/equal-row-and-column-pairs/description/
# Description: Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid_column = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                grid_column[i][j] = grid[j][i]

        counter = 0
        for i in range(n):
            for j in range(n):
                if grid_column[i] == grid[j]:
                    counter += 1

        return counter
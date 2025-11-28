# Problem: Pascal's Triangle
# LeetCode URL: https://leetcode.com/problems/pascals-triangle/description/
# Description: Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        lst = [[1],[1,1]]
        last_row_lst = [1]
        rows = 2
        while rows < numRows:
            for i in range(0,len(lst[-1])-1):
                last_row_lst.append(lst[-1][i] + lst[-1][i+1])
            last_row_lst.append(1)
            lst.append(last_row_lst)
            last_row_lst=[1]
            rows+=1
            

        return lst         


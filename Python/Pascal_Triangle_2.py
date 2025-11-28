# Problem: Pascal's Triangle 2
# LeetCode URL: https://leetcode.com/problems/pascals-triangle-ii/description/
# Description: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        lst = [[1],[1,1]]
        last_row_lst = [1]
        rows = 2
        while rows <= rowIndex:
            for i in range(0,len(lst[-1])-1):
                last_row_lst.append(lst[-1][i] + lst[-1][i+1])
            last_row_lst.append(1)
            lst.append(last_row_lst)
            if rowIndex-rows==0:
                return last_row_lst
            last_row_lst=[1]
            rows+=1

        return [] 

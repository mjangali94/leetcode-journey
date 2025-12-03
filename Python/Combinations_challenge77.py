# Problem: Combinations
# LeetCode https://leetcode.com/problems/combinations/description/
# Description: Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Medium level

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k>n:
            return []
        if k==0:
            return []
        result = []
        if k==1:
            for i in range(1,n+1):
                result.append([i])
            return result
        for i in range(n, 0, -1):
            sub_result = self.combine(i-1,k-1)
            if not sub_result:
                return result
            for a in sub_result:
                a.append(i)
                result.append(a)

        return result
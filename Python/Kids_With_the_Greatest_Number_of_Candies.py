# Problem: Kids With the Greatest Number of Candies
# LeetCode URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
# Description: There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        for i in candies:
            if i >= max_candy:
                max_candy = i
        result = [True for i in range(len(candies))]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_candy:
                result[i] =True
            else:
                result[i] =False
        return result
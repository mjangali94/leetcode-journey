# Problem: Valid Anagram
# LeetCode URL: https://leetcode.com/problems/valid-anagram/description/
# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = list(s)

        for a in t:
            if a in lst:
                lst.remove(a)
            else:
                return False
        if len(lst) == 0:
            return True
        return False
# Problem: Isomorphic Strings
# LeetCode URL: https://leetcode.com/problems/isomorphic-strings/description/
# Description: Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_st = {}
        map_ts = {}
        for a, b in zip(s,t):
            if a in map_st and map_st[a] != b:
                return False
            if b in map_ts and map_ts[b] != a:
                return False
            map_st[a] = b
            map_ts[b] = a
        
        return True
        

# Problem: First Unique Character in a String
# LeetCode URL: https://leetcode.com/problems/first-unique-character-in-a-string/description/
# Description: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        myMap = {}
        for i, a in enumerate(s):
            if a not in myMap:
                myMap[a] = i
            else:
                myMap[a] = -1
        for a,b in myMap.items():
            if b != -1:
                return b
        return -1
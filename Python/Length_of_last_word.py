# Problem: length of last word
# LeetCode URL: https://leetcode.com/problems/length-of-last-word
# Description: Given a string s consisting of words and spaces, return the length of the last word in the string.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while "  " in s:
            s = s.replace("  "," ")
        if s[-1] == ' ':
            s= s[:-1]
        return len(s.split(" ")[-1])
        
# Problem: Reverse Words in a String
# LeetCode https://leetcode.com/problems/reverse-words-in-a-string/description/
# Description: Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
# Medium level

class Solution:
    
    def reverseWords(self, s: str) -> str:
        while "  " in s:
            s=s.replace("  "," ")
        if s[-1]==" ":
            s = s[:-1]
        if s[0]==" ":
            s = s[1:]
        rList = []    
        sList = s.split(" ")
        rList = sList[::-1]
        
        return " ".join(rList)
# Problem: Merge Strings Alternately
# LeetCode URL: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# Description: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1),len(word2))
        result = ""
        for i in range(min_length):
            result += word1[i] + word2[i]
        
        if min_length < len(word1):
            result += word1[min_length:]
        elif min_length < len(word2):
            result += word2[min_length:]
        else:
            return result
        return result
        

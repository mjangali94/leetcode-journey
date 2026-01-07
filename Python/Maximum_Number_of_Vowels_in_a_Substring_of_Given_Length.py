# Problem: Maximum Number of Vowels in a Substring of Given Length
# LeetCode URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
# Description: Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        left, right = 0 , k-1
        cur_vowels = 0
        for i in range(k):
            if s[i] in "aeoiu":
               cur_vowels += 1
        if cur_vowels > max_vowels:
            max_vowels = cur_vowels
        while right < len(s) -1:
            right += 1
            if s[left] in "aeoiu" and s[right] not in "aeiou":
                cur_vowels -= 1
            elif s[left] not in "aeoiu" and s[right] in "aeiou":
                cur_vowels += 1
            left += 1
            if cur_vowels > max_vowels:
                max_vowels = cur_vowels
        return max_vowels
# Problem: Reverse Vowels of a String
# LeetCode URL: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Description: Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0 ,len(s)-1
        while left < right:
            while left < right and s[left].lower() not in "aeiou":
                left +=1
            while left < right and s[right].lower() not in "aeiou":
                right -=1
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1
        return "".join(s)

        
# Problem: Ransom Note
# LeetCode URL: https://leetcode.com/problems/ransom-note/description/
# Description: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst_magazine=list(magazine)
        for ch in ransomNote:
            if ch not in lst_magazine:
                return False
            else:
                lst_magazine.remove(ch)
        return True
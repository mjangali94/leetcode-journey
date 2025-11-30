# Problem: Word Pattern
# LeetCode URL: https://leetcode.com/problems/word-pattern/description/
# Description: Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        myMap_s = {}
        myMap_p = {}
        lst1 = list(pattern)
        lst2 = s.split()
        if len(lst1) != len(lst2):
            return False
        
        for a, b in zip(lst1,lst2):
            if a in myMap_s:
                if myMap_s[a] == b:
                    continue
                else:
                    return False
            else:
                if b in myMap_p:
                    if myMap_p[b] == a:
                        continue
                    else:
                        return False
                myMap_s[a] = b 
                myMap_p[b] = a
        return True

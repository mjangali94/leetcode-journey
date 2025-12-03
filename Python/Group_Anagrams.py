# Problem: Group Anagrams
# LeetCode URL: https://leetcode.com/problems/group-anagrams/description/
# Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Medium level

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for s in strs:
            key = "".join(sorted(s)) 
            if key not in myMap:
                myMap[key] = []
            myMap[key].append(s)
        return list(myMap.values())
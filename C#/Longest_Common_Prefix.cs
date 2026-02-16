// Problem: Longest Common Prefix
// LeetCode URL: https://leetcode.com/problems/longest-common-prefix/description/
// Description: Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".


public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs == null || strs.Length == 0)
            return "";

        for (int i = 0; i < strs[0].Length; i++)
        {
            char currentChar = strs[0][i];

            for (int j = 1; j < strs.Length; j++)
            {
                if (i >= strs[j].Length || strs[j][i] != currentChar)
                    return strs[0].Substring(0, i);
            }
        }

        return strs[0];
    }
}
// Problem: Palindrome Number
// LeetCode URL: https://leetcode.com/problems/palindrome-number/description/
// Description: Given an integer x, return true if x is a palindrome, and false otherwise.

 public class Solution
{
    public bool IsPalindrome(int x)
    {
        if (x < 0 || (x % 10 == 0 && x != 0))
            return false;

        int reversedHalf = 0;

        while (x > reversedHalf)
        {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        return x == reversedHalf || x == reversedHalf / 10;
    }
}
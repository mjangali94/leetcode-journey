# Problem: String to Integer (atoi)
# LeetCode URL: https://leetcode.com/problems/string-to-integer-atoi/description/
# Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

# Medium level

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == " ":
            i += 1
        
        if i == n:
            return 0
        
        is_negative = False
        if s[i] == "-":
            is_negative = True
            i += 1
        elif s[i] == "+":
            i += 1

        result = 0
        
        while i < n and ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
            digit = ord(s[i]) - ord("0")
            
            if result > (INT_MAX // 10) or (result == INT_MAX // 10 and digit > (7 if not is_negative else 8)):
                return INT_MIN if is_negative else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        return -result if is_negative else result
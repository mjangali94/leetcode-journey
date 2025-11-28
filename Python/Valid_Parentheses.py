# Problem: Valid Parentheses
# LeetCode URL: https://leetcode.com/problems/valid-parentheses
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""

        # if length is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False

        for ch in s:
            # opening brackets
            if ch in "({[":
                stack += ch

            # closing brackets
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack = stack[:-1]

            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack = stack[:-1]

            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack = stack[:-1]

        return stack == ""
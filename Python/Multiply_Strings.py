# Problem: Multiply Strings
# LeetCode URL: https://leetcode.com/problems/multiply-strings/description/
# Description: Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Medium level

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rows = []
        n1 = list(num1[::-1])
        n2 = list(num2[::-1])
        carry = 0
        row = []
        for i in range(len(n1)):
            for k in range(i):
                row.append('0')
            for j in range(len(n2)):
                mult = int(n1[i]) * int(n2[j]) + carry
                digit = mult % 10
                carry = mult // 10
                row.append(str(digit))
            if carry > 0:
                row.append(str(carry))
                carry =0
            if row:
                rows.append(row)
            row = []
        total = 0
        for i in rows:
            row = i[::-1]
            total += int("".join(row))
            
        return str(total)

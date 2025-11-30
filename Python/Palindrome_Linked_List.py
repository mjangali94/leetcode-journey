# Problem: Palindrome Linked List
# LeetCode URL: https://leetcode.com/problems/palindrome-linked-list/description/
# Description: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        stack = ""
        while head:
            stack += str(head.val)
            head = head.next
        
        n = len(stack)
        half = n // 2
        
        if n % 2 == 0:  # even length
            left = stack[:half]
            right = stack[half:]
        else:           # odd length
            left = stack[:half]
            right = stack[half+1:]
        
        return left == right[::-1]
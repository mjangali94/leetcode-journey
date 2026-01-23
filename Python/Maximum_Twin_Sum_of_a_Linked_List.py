# Problem: Maximum Twin Sum of a Linked List
# LeetCode URL: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Description: In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        lst.append(head.val)

        while head.next:
            head = head.next
            lst.append(head.val)
        
        left, right = 0, len(lst)-1
        max_sum = -float("inf")
        while left <= right :
            curr_sum = lst[left] + lst[right]
            max_sum = max(max_sum, curr_sum)
            left += 1
            right -= 1
        
        return max_sum
# Problem: Remove Nth Node From End of List
# LeetCode URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Description: Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Medium level
# challenge

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next=slow.next.next
        return dummy.next

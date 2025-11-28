# Problem: Intersection of Two Linked Lists
# LeetCode URL: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Description: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        lst=[]
        while headA:
            if headA not in lst:
                lst.append(headA)
            if not headA.next:
                break
            headA=headA.next

        while headB:
            if headB in lst:
                return headB
            if not headB.next:
                return None
            headB=headB.next
        return None

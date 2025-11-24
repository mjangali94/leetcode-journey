# Problem: Merge two sorted lists
# LeetCode URL: https://leetcode.com/problems/merge-two-sorted-lists
# Difficulty: Easy
# Description: You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        elif not list2:
            return list1

        
        if list1.val < list2.val:
            head = list1
            list1=list1.next
        elif list1.val >= list2.val:
            head = list2
            list2=list2.next
        
        list3 = head
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1=list1.next
            else:
                list3.next = list2
                list2=list2.next
            list3=list3.next
        
        if list1:
            list3.next = list1
        else:
            list3.next = list2
        return head

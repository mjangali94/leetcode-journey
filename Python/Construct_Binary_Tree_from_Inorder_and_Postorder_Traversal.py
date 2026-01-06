# Problem: Construct Binary Tree from Inorder and Postorder Traversal
# LeetCode URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Description: Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
# Medium level


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        head = TreeNode(postorder[-1])
        index = 0
        for i, a in enumerate(inorder):
            if a == postorder[-1]:
                index = i
                break
        
        head.left = self.buildTree(inorder[0:index], postorder[0:index])
        head.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return head

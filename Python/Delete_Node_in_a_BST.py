# Problem: Delete Node in a BST
# LeetCode URL: https://leetcode.com/problems/delete-node-in-a-bst/description/
# Description: Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.
# challenge


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1 & 2: node has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: node has 2 children
            # Find inorder successor (min in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

                
# Problem: Count Complete Tree Nodes
# LeetCode URL: https://leetcode.com/problems/count-complete-tree-nodes/description/
# Description: Given the root of a complete binary tree, return the number of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        

        

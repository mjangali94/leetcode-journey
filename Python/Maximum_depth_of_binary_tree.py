# Problem: Maximum Depth of Binary Tree
# LeetCode URL: https://leetcode.com/problems/maximum-depth-of-binary-tree
# Description: Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_max_depth= self.maxDepth(root.left)
        right_max_depth= self.maxDepth(root.right)
        if left_max_depth >= right_max_depth:
            return left_max_depth + 1
        else:
            return right_max_depth +1

        



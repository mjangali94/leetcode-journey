# Problem: Sum of Left Leaves
# LeetCode URL: https://leetcode.com/problems/sum-of-left-leaves/description/
# Description: Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return node.val if is_left else 0

            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)
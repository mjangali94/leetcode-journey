# Problem: Minimum Depth of Binary Tree
# LeetCode URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Description: Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            return self.minDepth(root.left) + 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        
        return min(self.minDepth(root.left),self.minDepth(root.right)) +1
        


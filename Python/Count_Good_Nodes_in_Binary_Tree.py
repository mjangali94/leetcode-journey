# Problem: Count Good Nodes in Binary Tree
# LeetCode URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# Description: Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# challenge


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, max_so_far: int):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            max_so_far = max(node.val, max_so_far)
            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
            
        return dfs(root, root.val)
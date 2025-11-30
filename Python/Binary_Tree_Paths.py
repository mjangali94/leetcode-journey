# Problem: Binary Tree Paths
# LeetCode URL: https://leetcode.com/problems/binary-tree-paths/description/
# Description: Given the root of a binary tree, return all root-to-leaf paths in any order.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        # If leaf node, return its value as a string in a list
        if not root.left and not root.right:
            return [str(root.val)]

        result = []

        if root.left:
            for path in self.binaryTreePaths(root.left):
                result.append(str(root.val) + "->" + path)

        if root.right:
            for path in self.binaryTreePaths(root.right):
                result.append(str(root.val) + "->" + path)

        return result

        

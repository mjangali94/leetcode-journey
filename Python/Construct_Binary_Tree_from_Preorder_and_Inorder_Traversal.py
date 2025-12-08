# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# LeetCode URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Description: Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# Medium level



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        head = TreeNode(preorder[0])
        index = 0
        for i, a in enumerate(inorder):
            if a == preorder[0]:
                index = i
                break
        
        head.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        head.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])

        return head






# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
#         index_map = {val: i for i, val in enumerate(inorder)}
#         self.post_idx = len(postorder) - 1
#         def build(left, right):

#             if left > right:
#                 return None

#             root_val = postorder[self.post_idx]
#             self.post_idx -= 1

#             root = TreeNode(root_val)
#             mid = index_map[root_val]
            
#             root.right = build(mid + 1, right)
#             root.left = build(left, mid - 1)

#             return root

#         return build(0, len(inorder) - 1)
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



# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         # Map inorder values to their index for O(1) split
#         index_map = {val: i for i, val in enumerate(inorder)}

#         # Postorder pointer (start from the end)
#         self.post_idx = len(postorder) - 1

#         def build(left, right):
#             # No nodes in this subtree
#             if left > right:
#                 return None

#             # Last element in postorder is the root
#             root_val = postorder[self.post_idx]
#             self.post_idx -= 1

#             root = TreeNode(root_val)

#             # Root index in inorder
#             mid = index_map[root_val]

#             # IMPORTANT: build right subtree first (postorder = L, R, ROOT)
#             root.right = build(mid + 1, right)
#             root.left = build(left, mid - 1)

#             return root

#         return build(0, len(inorder) - 1)
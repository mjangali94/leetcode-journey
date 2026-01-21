# Problem: Leaf-Similar Trees
# LeetCode URL: https://leetcode.com/problems/leaf-similar-trees/description/
# Description: Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaves(node: Optional[TreeNode], leaves: list[int]):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            find_leaves(node.left, leaves)
            find_leaves(node.right, leaves)

        leaf_1 = []
        leaf_2 = []

        find_leaves(root1, leaf_1)
        find_leaves(root2, leaf_2)

        return leaf_1 == leaf_2


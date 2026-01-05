# Problem: Binary Tree Level Order Traversal
# LeetCode URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Description: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# challenge

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result
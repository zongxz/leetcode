"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode):
        if root == None:
            return 0
        else:
            lmax = self.maxDepth(root.left) + 1
            rmax = self.maxDepth(root.right) + 1
            return max(lmax, rmax)

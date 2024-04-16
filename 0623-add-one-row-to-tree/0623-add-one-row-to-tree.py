# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
#         If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
        if depth == 1: return TreeNode(val, root, None)
    
        def traverse(node, currDepth):
            if not node:
                return
#             Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
            if currDepth == depth - 1: # start to add one row
                currLeft = node.left
                currRight = node.right
                node.left = TreeNode(val, left = currLeft)
                node.right = TreeNode(val, right = currRight)
                return node
            traverse(node.left, currDepth + 1)
            traverse(node.right, currDepth + 1)
            return node
        
        return traverse(root, 1)
                
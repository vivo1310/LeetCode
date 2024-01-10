# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # take a parent node, look at the children, swap them
        # now a child node become parent node, repeat that until no more child
        # q is the queue of parent nodes
        # print(root)
        q = [root]
        while q:
            parent = q.pop()
            # print('parent', parent)
            # add the children to the q waiting to be traversed
            if parent != None:
                if parent.left != None:
                    q.append(parent.left)
                if parent.right != None:
                    q.append(parent.right)

                # print(q)
                # swap the children
                parent.left, parent.right = parent.right, parent.left
            
        return root
        
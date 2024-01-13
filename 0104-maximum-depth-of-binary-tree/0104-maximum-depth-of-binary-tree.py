# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    
    # BFS: traverse level by level -> count number of level
    # BFS using queue
        # if not root:
        #     return 0
        # queue = [root]
        # count = 0
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         if node.left != None: 
        #             queue.append(node.left)
        #         if node.right != None:
        #             queue.append(node.right)
        #     count += 1
        # return count
        
        # DFS:
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
                
            
        
        
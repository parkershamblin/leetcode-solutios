# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = [root]
        while queue and root:
            result.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return result[::-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        InOrder(ls, root)
        return ls

def InOrder(ls: list, root: Optional[TreeNode]):
    if root:
        InOrder(ls, root.left)
        ls.append(root.val)
        InOrder(ls, root.right)

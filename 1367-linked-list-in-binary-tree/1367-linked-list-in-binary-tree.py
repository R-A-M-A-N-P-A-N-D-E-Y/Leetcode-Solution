# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False
        # Start dfs from the current root or continue from either child
        return self.dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, root: TreeNode, head: ListNode) -> bool:
        # If the list is exhausted, we've found a complete path
        if not head:
            return True
        # If the tree is exhausted, or values don't match, the path ends
        if not root or root.val != head.val:
            return False
        # Continue the search down both branches
        return self.dfs(root.left, head.next) or self.dfs(root.right, head.next)
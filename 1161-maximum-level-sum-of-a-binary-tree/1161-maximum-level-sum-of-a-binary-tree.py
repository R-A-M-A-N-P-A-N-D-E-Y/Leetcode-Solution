# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level = []
        level_size = len(q)

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ls = levelOrder(root)
        # print(ls)
        ans = 0
        temp = -1 * (10 ** 5)
        for i in range(len(ls)):
            if sum(ls[i]) > temp:
                temp = sum(ls[i])
                ans = i + 1
        
        return ans
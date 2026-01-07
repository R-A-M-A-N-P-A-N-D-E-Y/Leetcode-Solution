# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def treeSum(root):
#     if not root:
#         return 0

#     result = 0
#     q = deque([root])

#     while q:
#         node = q.popleft()
#         result += node.val

#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)

#     return result


# def maximum(root, totalSum):
#     if not root:
#         return 0

#     ans = 0
#     q = deque([root])

#     while q:
#         node = q.popleft()
#         subsum = treeSum(node)
#         ans = max(ans, (totalSum - subsum) * subsum)

#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)

#     return ans


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subsum = left + right + node.val
            self.ans = max(self.ans, subsum * (totalSum - subsum))

            return subsum

        # Step 1: compute total sum
        def treeSum(root):
            if not root:
                return 0
            return root.val + treeSum(root.left) + treeSum(root.right)

        totalSum = treeSum(root)

        # Step 2: compute max product using DFS
        dfs(root)

        return self.ans % MOD

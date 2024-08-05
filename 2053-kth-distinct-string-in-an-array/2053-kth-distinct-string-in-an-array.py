class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        visited = []
        ans = []

        for i in range(len(arr)):
            if arr[i] not in visited:
                visited.append(arr[i])
                ans.append(arr[i])
            elif arr[i] in visited and arr[i] in ans:
                ans.remove(arr[i])

        return ans[k-1] if k <= len(ans) else ""
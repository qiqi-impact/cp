class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(node, cur, p):
            if not node: return
            nonlocal ans
            cur += node.val
            ans += p.get(cur - targetSum, 0)
            p[cur] += 1
            for ch in node.left, node.right:
                dfs(ch, cur, p)
            p[cur] -= 1
        d = defaultdict(int)
        d[0] = 1
        dfs(root, 0, d)
        return ans
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            ret = defaultdict(int)
            ret[node.val] = 1
            for ch in node.left, node.right:
                if ch:
                    d = dfs(ch)
                    for k in d:
                        ret[node.val + k] += d[k]
            ans += ret[targetSum]
            return ret
        if root: dfs(root)
        return ans
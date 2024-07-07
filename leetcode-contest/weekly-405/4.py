class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        root = {}
        KEY = '-'

        def ins(node, w, cost):
            cur = root
            for i in range(len(w)):
                c = w[i]
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                if i == len(w)-1:
                    cur[KEY] = min(cur.get(KEY, inf), cost)
        for i in range(len(words)):
            ins(root, words[i], costs[i])
        
        @cache
        def dp(idx):
            if idx == len(target):
                return 0
            cur = root
            ret = inf
            for i in range(idx, len(target)):
                if target[i] not in cur:
                    break
                cur = cur[target[i]]
                if '-' in cur:
                    ret = min(ret, dp(i+1) + cur['-'])
            return ret
        q = dp(0)
        return q if q != inf else -1     
                    
        
        
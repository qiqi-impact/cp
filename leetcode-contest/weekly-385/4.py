class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        root = {}
        
        def ins(node, w, idx):
            cur = root
            for i in range(len(w)):
                x = w[i] + w[-1-i]
                if x not in cur:
                    cur[x] = {}
                cur = cur[x]
                if i == len(w)-1:
                    if 'fwd' not in cur:
                        cur['fwd'] = 0
                    cur['fwd'] += 1
        
        ret = 0
        def check(node, w, idx):
            r = 0
            cur = root
            for i in range(len(w)):
                x = w[i] + w[-1-i]
                if x not in cur:
                    cur[x] = {}
                cur = cur[x]
                if 'fwd' in cur:
                    r += cur['fwd']
            return r
        
        for i in range(len(words)):
            ret += check(root, words[i], i)
            ins(root, words[i], i)
        return ret
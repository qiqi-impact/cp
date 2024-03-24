class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = {}
        
        def ins(node, w, idx):
            cur = root
            l = [cur]
            for i in range(len(w)):
                c = w[i]
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                l.append(cur)
                if i == len(w)-1:
                    for cur in l:
                        if '_' not in cur:
                            cur['_'] = (inf, inf)
                        cur['_'] = min(cur['_'], (len(w), idx))
                    
        def fin(node, w):
            cur = root
            for i in range(len(w)):
                c = w[i]
                if c not in cur:
                    break
                cur = cur[c]
            return cur['_'][1]
            
        for i, w in enumerate(wordsContainer):
            ins(root, w[::-1], i)
            
        ret = []
        for w in wordsQuery:
            ww = w[::-1]
            ret.append(fin(root, ww))
        return ret
            
            
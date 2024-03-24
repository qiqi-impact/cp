root = {}
KEY = '-'
        
def ins(node, w):
    cur = root
    for i in range(len(w)):
        c = w[i]
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
        if i == len(w)-1:
            cur[KEY] = cur.get(KEY, 0) + 1
            
def fin(node, w):
    cur = root
    for i in range(len(w)):
        c = w[i]
        if c not in cur:
            # not found
            return 0
        cur = cur[c]
    return cur.get(KEY, 0)
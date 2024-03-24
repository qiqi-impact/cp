root = {}
        
def ins(node, w, idx):
    cur = root
    for i in range(len(w)):
        c = w[i]
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
        if i == len(w)-1:
            cur['-'] = True
            
def fin(node, w):
    cur = root
    for i in range(len(w)):
        c = w[i]
        if c not in cur:
            break
        cur = cur[c]
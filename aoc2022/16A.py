nodes = {}

with open('in') as f:
    for l in f.read().splitlines():
        name = l[6:8]
        cur = 0
        for c in l:
            if '0' <= c <= '9':
                cur = cur * 10 + int(c)
        q = l.find('valves ')
        if q == -1:
            idx = l.find('valve ')+len('valve ')
        else:
            idx = l.find('valves ')+len('valves ')
        adj = l[idx:].split(', ')
        nodes[name] = (name, cur, adj)

path = []

@cache
def dfs(last_vertex, visited_vertices):
    pass
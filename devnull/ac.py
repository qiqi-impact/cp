from collections import defaultdict

K = 26

class Vertex:
    def __init__(self, p=-1, pch='$'):
        self.leaf = False
        self.next = [-1]*K
        self.go = [-1]*K
        self.parent = p
        self.pch = pch
        self.link = -1

t = [Vertex()]

def add_string(s):
    v = 0
    for ch in s:
        c = ord(ch) - 97
        if t[v].next[c] == -1:
            t[v].next[c] = len(t)
            t.append(Vertex(v, ch))
        v = t[v].next[c]
    t[v].leaf = True

def get_link(v):
    if t[v].link == -1:
        if v == 0 or t[v].p == 0:
            t[v].link = 0
        else:
            t[v].link = go(get_link(t[v].p), t[v].pch)
    return t[v].link

def go(v, ch):
    c = ord(ch) - 97
    if t[v].go[c] == -1:
        if t[v].next[c] == -1:
            t[v].go[c] = go(get_link(v), ch) if v else 0
        else:
            t[v].go[c] = t[v].next[c]
    return t[v].go[c]

def search_words(text):
    pass



print(search_words('sadfsadfsafd'))
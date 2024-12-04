from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math

class Node:
    def __init__(self):
        self.val = self.left = self.right = self.p = None
    def add(self, node):
        n = Node()
        self.p = node.p = n
        n.left = self
        n.right = node
        n.clean()
        return n

    def rep(self):
        if self.is_pair():
            return '[{},{}]'.format(self.left.rep(), self.right.rep())
        else:
            return self.val

    def mag(self):
        if self.is_pair():
            return 3 * self.left.mag() + 2 * self.right.mag()
        else:
            return self.val

    def is_pair(self):
        return self.val is None

    def add_left(self, v):
        cur, p = self, self.p
        while p:
            if p.left != cur:
                cur = p.left
                break
            cur, p = p, p.p
        if p:
            while cur.right:
                cur = cur.right
            cur.val += v

    def add_right(self, v):
        cur, p = self, self.p
        while p:
            if p.right != cur:
                cur = p.right
                break
            cur, p = p, p.p
        if p:
            while cur.left:
                cur = cur.left
            cur.val += v

    def kill(self):
        p = self.p
        n = Node()
        n.p = p
        n.val = 0
        if self.p.left == self:
            self.p.left = n
        else:
            self.p.right = n

    def explode(self, depth):
        if self.is_pair():
            if depth == 4:
                # print(self.left.val, self.right.val)
                self.add_left(self.left.val)
                self.add_right(self.right.val)
                self.kill()
                return True
            else:
                if self.left.explode(depth+1):
                    return True
                if self.right.explode(depth+1):
                    return True
        return False

    def split(self):
        if self.is_pair():
            if self.left.split():
                return True
            if self.right.split():
                return True
        elif self.val >= 10:
            l = Node()
            l.val = self.val//2
            l.p = self
            r = Node()
            r.val = (self.val+1)//2
            r.p = self
            self.left = l
            self.right = r
            self.val = None
            return True
        return False

    def clean(self):
        while 1:
            # print(self.rep())
            if self.explode(0):
                continue
            if self.split():
                continue
            break

cur = None
with open('in') as f:
    for line in f.read().splitlines():
        st = []
        for c in line:
            if '0' <= c <= '9':
                n = Node()
                n.val = int(c)
                st.append(n)
            elif c == ']':
                r = st.pop()
                l = st.pop()
                st.append(l.add(r))
        if cur:
            cur = cur.add(st[0])
        else:
            cur = st[0]
print(cur.mag())
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 3:
            return trees
        
        def order(p):
            if p[0] == 0:
                if p[1] == 0:
                    return (-inf, -inf)
                return (math.pi/2, p[0]+p[1])
            x = math.atan(p[1]/p[0])
            if x < 0:
                x += math.pi
            return (x, p[0]+p[1])
        
        def crossproduct(a, b, c):
            return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])
        
        my, mx = inf, inf
        for x, y in trees:
            if y < my:
                my = y
                mx = x
            elif y == my:
                mx = min(mx, x)
        
        trees = [(x-mx, y-my) for (x, y) in trees]
        l = [(order(t), t) for t in trees]
        l.sort()
        
        ret = [0, 1]
        ptr = 2
        for ptr in range(2, len(l)):
            while 1:
                p1, p2, p3 = l[ret[-2]][1], l[ret[-1]][1], l[ptr][1]
                v = crossproduct(p1, p2, p3)
                if v < 0:
                    ret.pop()
                else:
                    break
            ret.append(ptr)
        
        for i in range(1, len(l)-1):
            if crossproduct(l[-1][1], l[i][1], l[0][1]) == 0:
                ret.append(i)
            
        return [(l[p][1][0]+mx, l[p][1][1]+my) for p in list(set(ret))]
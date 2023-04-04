class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = {}
        ind = {}
        
        for i in range(len(recipes)):
            ind[recipes[i]] = len(ingredients[i])
            for x in ingredients[i]:
                if x not in g:
                    g[x] = []
                g[x].append(recipes[i])
        
        ret = []
        q = deque(supplies)
        while q:
            cur = q.popleft()
            for x in g.get(cur, []):
                ind[x] -= 1
                if ind[x] == 0:
                    q.append(x)
                    ret.append(x)
        
        return ret
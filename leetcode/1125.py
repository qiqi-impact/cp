class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {}
        for i, sk in enumerate(req_skills):
            d[sk] = i
        FULL = (1 << len(req_skills)) - 1
        
        bp = []
        for p in people:
            cur = 0
            for sk in p:
                cur ^= (1 << d[sk])
            bp.append(cur)
        
        @cache
        def dp(idx, b):
            if b == FULL:
                return [0, []]
            if idx == len(people):
                return [1e9, []]
            ret = dp(idx+1, b)
            x, y = dp(idx+1, b | bp[idx])
            if x + 1 < ret[0]:
                ret = [x+1, y+[idx]]
            return ret
            
        return dp(0, 0)[1]
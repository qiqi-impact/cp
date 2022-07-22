class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # Normalize the hat numbers to 0, 1, 2, ...
        norm = set()
        for l in hats:
            for x in l:
                norm.add(x)
        norm = list(norm)
        rev = {}
        for i in range(len(norm)):
            rev[norm[i]] = i
            
        # Convert hat numbers in list to normalized numbers
        hat_count = len(norm)
        ppl_count = len(hats)
        people_who_like_hat = [0] * hat_count
        for i in range(len(hats)):
            hats[i] = set([rev[x] for x in hats[i]])
            for x in hats[i]:
                people_who_like_hat[x] ^= (1 << i)
        
        # number of ways to assign the remaining hats if we are on the idx-th hat and have assigned (taken as a bitfield) people
        @cache
        def dp(idx, taken):
            # we assigned all hats
            if taken == (1 << ppl_count) - 1:
                return 1
            
            # we ran out of hats to give
            if idx == hat_count:
                return 0
            
            # possibilities:
            # 1. skip this hat
            ret = dp(idx+1, taken)
            
            for i in range(ppl_count):
                b = 1 << i
                # 2. if a person isn't taken and likes this hat, take it
                if taken & b == 0 and (people_who_like_hat[idx] & b):
                    ret += dp(idx+1, taken ^ b)
            ret %= 10**9+7
            return ret
        return dp(0, 0)
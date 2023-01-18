class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        pf = [0]
        for c in floor:
            pf.append(pf[-1] + int(c == '1'))
        
        @cache
        def dp(idx, left):
            if len(floor) - idx <= left * carpetLen:
                return 0
            if not left:
                return pf[-1] - pf[idx]
            if floor[idx] == '0':
                return dp(idx+1, left)
            
            end = min(len(floor) - 1, idx + carpetLen - 1)
            if pf[end+1] - pf[idx] == end - idx + 1:
                return dp(idx + carpetLen, left - 1)
            
            ret = 1 + dp(idx+1, left)
            if floor[idx] == '1':
                ret = min(ret, dp(min(idx + carpetLen, len(floor)), left - 1))
            return ret
        return dp(0, numCarpets)
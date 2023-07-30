class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        best = None
        
        for x, y, z in permutations([a, b, c]):
            if y not in x:
                for ovr in range(len(x), -1, -1):
                    if x[len(x)-ovr:] == y[:ovr]:
                        x += y[ovr:]
                        break
                        
            if z not in x:
                for ovr in range(len(x), -1, -1):
                    if x[len(x)-ovr:] == z[:ovr]:
                        x += z[ovr:]
                        break
            
            if best is None or len(best) > len(x) or (len(best) == len(x) and x < best):
                best = x
        
        return best


                
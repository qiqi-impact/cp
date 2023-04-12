class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        D = {
            'R': [0, 1],
            'L': [0, -1],
            'U': [-1, 0],
            'D': [1, 0]
        }
        
        s = [D[c] for c in s]
        
        ret = []
        for i in range(len(s)):
            cur = 0
            cx, cy = startPos
            for j in range(i, len(s)):
                dx, dy = s[j]
                nx, ny = cx+dx, cy+dy
                if not (0 <= nx < n) or not (0 <= ny < n):
                    break
                cur += 1
                cx, cy = nx, ny
            ret.append(cur)
        return ret
                
        
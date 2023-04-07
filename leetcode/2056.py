class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def simulate(dests):
            pcs = [positions[i][:] for i in range(len(positions))]
            dirs = []
            for i in range(len(dests)):
                dx = dests[i][0] - pcs[i][0]
                dy = dests[i][1] - pcs[i][1]
                if dx < 0:
                    dx = -1
                elif dx > 0:
                    dx = 1
                if dy < 0:
                    dy = -1
                elif dy > 0:
                    dy = 1
                dirs.append([dx, dy])
            for t in range(7):
                for i in range(len(pcs)):
                    if pcs[i][0] != dests[i][0] or pcs[i][1] != dests[i][1]:
                        pcs[i][0] += dirs[i][0]
                        pcs[i][1] += dirs[i][1]
                s = set([tuple(x) for x in pcs])
                if len(s) < len(pcs):
                    return False
            return True
        
        CHANGE = {
            'rook': [[-1,0],[1,0],[0,-1],[0,1]],
            'bishop': [[-1,-1],[1,-1],[-1,1],[1,1]]
        }
        CHANGE['queen'] = CHANGE['rook'] + CHANGE['bishop']
        
        ret = 0
        dests = []
        def dfs(idx):
            nonlocal ret
            if idx == len(pieces):
                if simulate(dests):
                    ret += 1
                return
            
            dests.append(positions[idx])
            dfs(idx+1)
            dests.pop()
            
            for dx, dy in CHANGE[pieces[idx]]:
                for i in range(1, 8):
                    nx, ny = [positions[idx][0] + i * dx, positions[idx][1] + i * dy]
                    if 1 <= nx <= 8 and 1 <= ny <= 8:
                        dests.append([nx, ny])
                        dfs(idx+1)
                        dests.pop()
                    else:
                        break
        dfs(0)
        return ret
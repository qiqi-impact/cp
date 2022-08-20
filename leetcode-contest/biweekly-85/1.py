class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ret = len(blocks)
        for i in range(len(blocks)-k+1):
            n = 0
            for j in range(i, i+k):
                n += int(blocks[j] == 'W')
            ret = min(ret, n)
        return ret
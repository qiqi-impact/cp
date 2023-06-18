class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ret = 0
        ct = 0
        while mainTank:
            ret += 10 * mainTank
            ct += mainTank
            mainTank = min(additionalTank, ct // 5)
            ct %= 5
            additionalTank -= mainTank
        return ret
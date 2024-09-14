class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ret = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                ret.append(i)
        return ret
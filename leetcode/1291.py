class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        X = '123456789'
        ret = []
        for i in range(len(X)):
            for j in range(i+1, len(X)+1):
                v = int(X[i:j])
                if low <= v <= high:
                    ret.append(v)
        return sorted(ret)
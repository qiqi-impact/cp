class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ret = []
        def f(left, arr):
            if left == 1:
                if 0 not in arr:
                    return False
                ret.append(sum(arr))
                return True
            v = arr[1] - arr[0]
            freq = Counter(arr)
            l, r = [], []
            for x in arr:
                if freq[x] > 0:
                    if freq[x+v] == 0:
                        return False
                    freq[x] -= 1
                    freq[x+v] -= 1
                    l.append(x)
                    r.append(x+v)
            ret.append(v)
            if f(left - 1, l):
                return True
            ret.pop()
            ret.append(-v)
            if f(left - 1, r):
                return True
            ret.pop()
        f(n, sums)
        return ret
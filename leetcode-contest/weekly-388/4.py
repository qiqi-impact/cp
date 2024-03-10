class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        arr = [[[None for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        
        for idx in range(n, -1, -1):
            for b in range(2):
                for q in range(k+1):
                    amt = q - 1
                    if idx == n:
                        r = -inf if amt != k-1 else 0
                    else:
                        r = -inf
                        v = nums[idx]
                        if b:
                            if amt%2 == 0:
                                r = max(r, (k-amt) * v + arr[idx+1][1][q])
                            else:
                                r = max(r, (k-amt) * -v + arr[idx+1][1][q])
                        if amt != k-1:
                            r = max(r, (k-amt-1) * (v if amt%2 else -v) + arr[idx+1][1][q+1])
                        r = max(r, arr[idx+1][0][q])
                    arr[idx][b][q] = r
        return arr[0][0][0]
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = [gas[i] - cost[i] for i in range(len(gas))]
        sm = 0
        mn = float('inf')
        idx = 0
        for i in range(len(l)):
            sm += l[i]
            if sm < mn:
                mn = sm
                idx = (i+1)%len(l)
        cur = 0
        for i in range(idx, idx+len(l)):
            cur += gas[i%len(l)]
            if cur < cost[i%len(l)]:
                return -1
            cur -= cost[i%len(l)]
        return idx
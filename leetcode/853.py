class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = list(zip(position, speed))
        l.sort()
        
        t = [(target - l[i][0])/l[i][1] for i in range(len(l))]
        mx = 0
        ret = 0
        for i in range(len(t)-1, -1, -1):
            if t[i] > mx:
                ret += 1
                mx = t[i]
        return ret
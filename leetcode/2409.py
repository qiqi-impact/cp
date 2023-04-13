class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        xx = [0]
        for t in x:
            xx.append(xx[-1] + t)
        
        a, b = arriveAlice.split('-')
        a, b = int(a), int(b)
        A = xx[a-1] + b-1
        
        a, b = leaveAlice.split('-')
        a, b = int(a), int(b)
        B = xx[a-1] + b-1
        
        a, b = arriveBob.split('-')
        a, b = int(a), int(b)
        C = xx[a-1] + b-1
        
        a, b = leaveBob.split('-')
        a, b = int(a), int(b)
        D = xx[a-1] + b-1
        
        if C > B or A > D:
            return 0
        
        if A > C:
            A,B,C,D = C,D,A,B
            
        if C >= A and D <= B:
            return D - C + 1
        
        return B - C + 1
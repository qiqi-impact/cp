class Solution:
    def isCircularSentence(self, q: str) -> bool:
        q = q.split(' ')
        for i in range(len(q)):
            if q[i][-1] != q[(i+1)%len(q)][0]:
                return False
        return True
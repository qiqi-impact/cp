class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        ret = len(t)
        
        left = [len(s)] * len(t)
        tp = 0
        for i in range(len(s)):
            if s[i] == t[tp]:
                left[tp] = i
                ret = min(ret, len(t) - 1 - tp)
                tp += 1
            if tp == len(t):
                return 0
        
        right = [-1] * len(t)
        tp = len(t)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] == t[tp]:
                right[tp] = i
                ret = min(ret, tp)
                tp -= 1
        
        j = -1
        for i in range(1, len(t)):
            while j+1 < i and left[j+1] < right[i]:
                j += 1
            if j != -1:
                ret = min(ret, i - j - 1)
        return ret
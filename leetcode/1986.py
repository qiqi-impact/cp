class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        @cache
        def pack(idx, ss):
            if idx == n:
                return len(ss)
            l = list(ss)
            t = tasks[idx]
            ret = pack(idx+1, tuple(sorted(l + [t])))
            for i in range(len(l)):
                if l[i] + t <= sessionTime:
                    l[i] += t
                    ret = min(ret, pack(idx+1, tuple(sorted(l))))
                    l[i] -= t
            return ret
        return pack(0, tuple())
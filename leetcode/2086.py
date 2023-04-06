class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = set()
        for i in range(len(hamsters)):
            v = hamsters[i]
            if v == 'H':
                if i-1 in s:
                    continue
                if i+1 == len(hamsters) or hamsters[i+1] == 'H':
                    if i == 0 or hamsters[i-1] == 'H':
                        return -1
                    s.add(i-1)
                    continue
                s.add(i+1)
        return len(s)
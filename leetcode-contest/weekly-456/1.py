class Solution:
    def partitionString(self, s: str) -> List[str]:
        q = set()
        cur = ''
        ret = []
        for c in s:
            cur += c
            if cur not in q:
                ret.append(cur)
                q.add(cur)
                cur = ''
        return ret
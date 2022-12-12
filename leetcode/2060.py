class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        #diff is num chars run through in s1 - those in s2
        @cache
        def f(p1, p2, diff):
            # print(p1, p2, diff)
            if p1 == len(s1) and p2 == len(s2):
                return diff == 0
            if p1 < len(s1) and p2 < len(s2) and diff == 0 and 'a' <= s1[p1] <= 'z' and 'a' <= s2[p2] <= 'z' and s1[p1] != s2[p2]:
                return False
            if p1 == len(s1) or diff > 0:
                if p2 == len(s2):
                    return False
                v = s2[p2]
                if 'a' <= v <= 'z':
                    if f(p1, p2+1, diff-1):
                        return True
                else:
                    sm = 0
                    for digits in range(3):
                        if p2 + digits < len(s2):
                            if 'a' <= s2[p2 + digits] <= 'z':
                                break
                            sm = 10 * sm + int(s2[p2 + digits])
                            if f(p1, p2 + digits + 1, diff - sm):
                                return True
            else:
                if p1 == len(s1):
                    return False
                v = s1[p1]
                if 'a' <= v <= 'z':
                    if f(p1+1, p2, diff+1):
                        return True
                else:
                    sm = 0
                    for digits in range(3):
                        if p1 + digits < len(s1):
                            if 'a' <= s1[p1 + digits] <= 'z':
                                break
                            sm = 10 * sm + int(s1[p1 + digits])
                            if f(p1 + digits + 1, p2, diff + sm):
                                return True
            return False
        return f(0, 0, 0)
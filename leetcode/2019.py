class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        st = [int(s[0])]
        for i in range(1, len(s), 2):
            if s[i] == '+':
                st.append(int(s[i+1]))
            else:
                st[-1] *= int(s[i+1])
        ans = sum(st)
        
        @cache
        def dp(l, r):
            if l == r:
                return set([int(s[l])])
            ret = set()
            for i in range(l+1, r, 2):
                ls = dp(l, i-1)
                rs = dp(i+1, r)
                for x in ls:
                    for y in rs:
                        if s[i] == '+':
                            if x + y <= 1000:
                                ret.add(x + y)
                        else:
                            if x * y <= 1000:
                                ret.add(x * y)
            return ret
        
        wrong = dp(0, len(s)-1)
        
        ret = 0
        for n in answers:
            if n == ans:
                ret += 5
            elif n in wrong:
                ret += 2
        return ret
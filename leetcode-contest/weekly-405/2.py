class Solution:
    def validStrings(self, n: int) -> List[str]:
        l = ['0', '1']
        for i in range(n-1):
            nl = []
            for x in l:
                if x[-1] == '1':
                    nl.append(x + '0')
                nl.append(x + '1')
            l = nl
        return l
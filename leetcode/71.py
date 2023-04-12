class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []
        cur = ''
        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if ret:
                        ret.pop()
                elif cur == '.':
                    pass
                elif cur != '':
                    ret.append(cur)
                cur = ''
            else:
                cur += c
        return '/' + '/'.join(ret)
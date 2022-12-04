class Solution:
    def convertToTitle(self, c: int) -> str:
        ret = []
        while c:
            ret.append(ascii_uppercase[(c-1)%26])
            c = (c - (c-1)%26)//26
        ret = ret[::-1]
        return ''.join(ret)
class Solution:
    def checkTwoChessboards(self, a: str, b: str) -> bool:
        x = (ord(a[0])-97) - int(a[1])
        y = (ord(b[0])-97) - int(b[1])
        return (x - y) % 2 == 0
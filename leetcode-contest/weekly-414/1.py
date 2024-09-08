class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l = date.split('-')
        l = [bin(int(x))[2:] for x in l]
        return '-'.join(l)
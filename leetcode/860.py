class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a, b = 0, 0
        for x in bills:
            xx = x - 5
            nb = min(b, xx//10)
            xx -= nb * 10
            b -= nb
            na = min(a, xx//5)
            xx -= na * 5
            a -= na
            if xx:
                return False
            if x == 10:
                b += 1
            if x == 5:
                a += 1
        return True
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        tp = 0
        for i in range(1, 100000):
            adv = False
            for c in source:
                if c == target[tp]:
                    adv = True
                    tp += 1
                    if tp == len(target):
                        return i
            if not adv:
                return -1
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ret = 0
        for x in details:
            if int(x[-4:-2]) > 60:
                ret += 1
        return ret
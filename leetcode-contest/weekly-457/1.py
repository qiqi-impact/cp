class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        l = []
        for i in range(len(code)):
            if not code[i]:
                continue
            if not isActive[i]:
                continue
            if businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue
            fail = False
            c = code[i]
            for x in c:
                if not (x.isalpha() or x.isdigit() or x == '_'):
                    fail = True
                    break
            if not fail:
                l.append(i)

        def order(k):
            idx = ["electronics", "grocery", "pharmacy", "restaurant"].index(businessLine[k])
            return (idx, code[k])

        l.sort(key=order)
        return [code[k] for k in l]
            
def numberOfItems(s, si, ei):
    ans = []
    for a, b in zip(si, ei):
        foundbar = False
        cur = 0
        ret = 0
        for i in range(a-1, b):
            if s[i] == '|':
                if not foundbar:
                    foundbar = True
                else:
                    ret += cur
                    cur = 0
            else:
                cur += 1
        ans.append(ret)
    return ans

S = '|**|*|*'
startIndices = [1, 1]
endIndices = [5, 6]

print(numberOfItems(S, startIndices, endIndices))
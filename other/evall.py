# s = '338*3338*33338*333338+3333338*33333338+333333338'
s = '338*3338*33338*333338+3333338*33333338+333333338'

ret = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i].isdigit() and s[j].isdigit():
            ret += eval(s[i:j+1])
            ret %= 998244353
print(ret)
for _ in range(int(input())):
    n = int(input())
    
    ta = list(map(int, input().split()))
    tb = list(map(int, input().split()))
    
    a = [(x, y) for x, y in zip(ta, tb)]
    a.sort()
    
    cnt = [0] * (n + 1)
    pr = 0
    ans = 0
    
    for i in range(n):
        print(a[i])
        if pr != a[i][0]:
            pr = a[i][0]
            
            if pr * pr > 2 * n:
                break
                
            cnt = [0] * (n + 1)
            for j in range(i + 1, n):
                t = a[i][0] * a[j][0] - a[j][1]
                if 1 <= t <= n:
                    cnt[t] += 1
        print(cnt)
        ans += cnt[a[i][1]]
        
        if i + 1 < n:
            t = a[i][0] * a[i + 1][0] - a[i + 1][1]
            if 1 <= t <= n:
                cnt[t] -= 1
        print(cnt)
    
    print(ans)
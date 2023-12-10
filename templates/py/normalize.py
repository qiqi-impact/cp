def normalize(arr):
    ll = sorted(set(arr))
    m = {ll[i]:i for i in range(len(ll))}
    return [m[x] for x in arr]
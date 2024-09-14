#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

struct dsu {
    vector<int> p;
    vector<int> sz;
    int n;

    dsu(int _n) : n(_n) {
        p = vector<int>(n);
        iota(p.begin(), p.end(), 0);
        sz = vector<int>(n, 1);
    }

    inline int get(int x) {
        if (p[x] == x) {
            return x;
        } else {
            return p[x] = get(p[x]);
        }
    }

    inline bool unite(int x, int y) {
        x = get(x);
        y = get(y);
        if (x == y) {
            return false;
        }
        p[x] = y;
        sz[y] += sz[x];
        return true;
    }

    inline bool same(int x, int y) {
        return (get(x) == get(y));
    }

    inline int size(int x) {
        return sz[get(x)];
    }

    inline bool root(int x) {
        return (x == get(x));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    for (int qq = 1; qq <= tt; qq++) {
        cout << "Case #" << qq << ": ";
        int n;
        cin >> n;
        vector<int> p(n);
        for (int i = 0; i < n; i++) {
            cin >> p[i];
            p[i]--;
        }
        dsu uf(n);
        for (int i = 0; i < n; i++) {
            uf.unite(i, p[i]);
        }
        vector<int> dp(n + 1, 5 * n);
        dp[0] = -1;
        map<int, int> cnt;
        for (int i = 0; i < n; i++) {
            if (uf.root(i)) {
                cnt[uf.size(i)]++;
            }
        }
        debug(cnt);
        for (auto [x, y] : cnt) {
            vector<int> new_dp(n + 1, 5 * n);
            for (int d = 0; d < x; d++) {
                deque<int> deq;
                for (int it = 0; it * x + d <= n; it++) {
                    auto Get = [&](int when) {
                        return dp[when * x + d] + (it - when);
                    };
                    while (!deq.empty() && Get(deq.back()) >= Get(it)) {
                        deq.pop_back();
                    }
                    deq.emplace_back(it);
                    new_dp[it * x + d] = Get(deq.front());
                    if (deq.front() == it - y) {
                        deq.pop_front();
                    }
                }
            }
            swap(dp, new_dp);
        }
        int best = 5 * n;
        for (int i = n; i >= 0; i--) {
            dp[i] = min(dp[i], best + 1);
            best = min(best, dp[i]);
        }
        for (int i = 1; i <= n; i++) {
            cout << dp[i] << " \n"[i == n];
        }
    }
    return 0;
}
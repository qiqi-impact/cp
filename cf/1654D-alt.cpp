#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define vi vector<int>
#define pi pair<int, int>
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}
using namespace std;
const int maxn = 200005;
int fl[maxn];
int mn[maxn]; // max minus
int hv[maxn];
int cur[maxn];
#define ar3 array<int, 3>
vector<ar3> eg[maxn];
 
vi vis;
int n;
ll sum = 0;
vector<pi> prs[maxn];
bool bpr[maxn];
int dep[maxn];

ll cres = 0;
 
void ins(int id, int tp) {
    for (auto v : prs[id]) {
        int f = v.fi, g = v.se;
        if (!hv[f]) {
            hv[f] = 1;
            vis.pb(f);
        }
        cur[f] += tp * g;
        chkmin(mn[f], cur[f]);
    }
    if (tp == 1) cres = cres * id % mod;
    else cres = cres * ksm(id, mod - 2) % mod;
}
void dfs(int a, int fa) {
    dep[a] = 1;
    sum = (sum + cres) % mod;
    for (auto v : eg[a]) {
        if (v[0] == fa) continue;
        ins(v[2], 1);
        ins(v[1], -1);
        dfs(v[0], a);
        ins(v[1], 1);
        ins(v[2], -1);
    }
}
int main() {
    int t;
    cin >> t;
    for (int i = 0; i < maxn; i++) bpr[i] = 1;
    for (int i = 2; i < maxn; i++) {
        if (bpr[i]) {
            for (int j = i; j < maxn; j += i) {
                bpr[j] = 0;
                int cur = 0, cr = j;
                while (cr % i == 0)
                    cur += 1, cr /= i;
                prs[j].pb(mp(i, cur));
            }
        }
    }
    while (t--) {
        cin >> n;
        for (int i = 1; i <= n; i++) eg[i].clear(), dep[i] = 0;
        for (int i = 1; i < n; i++) {
            int u, j, x, y;
            scanf("%d%d%d%d", &u, &j, &x, &y);
            eg[u].pb({j, x, y});
            eg[j].pb({u, y, x});
        }
        // cur : current
        ll ans = 0;
        for (int i = 1; i <= n; i++)
            if (!dep[i]) {
                sum = 0;
                cres = 1;
                dfs(i, 0);
                ll coeff = 1;
                for (auto j : vis) {
                    coeff *= ksm(j, -mn[j]);
                    coeff %= mod;
                    mn[j] = hv[j] = cur[j] = 0;
                }
                sum *= coeff;
                sum %= mod;
                ans = (ans + sum) % mod;
            }
        cout << ans << endl;
    }
    return (0-0); //<3
}
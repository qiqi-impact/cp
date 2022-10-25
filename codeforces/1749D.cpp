#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

const ll MOD = 998244353LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    ll m;
    cin >> n >> m;
    ll cur = 1;
    ll prod = m%MOD;
    
    ll tot = 0;
    ll pw = 1;

    
    for (int i = 1;i <= n;i++) {
        pw *= m%MOD;
        if (i!=1) tot += pw;
        pw %= MOD;
        tot %= MOD;
    }
    // cout << tot << endl;

    vector<int> pr(1000, true);

    for (int i = 2;i <= n;i++) {
        if (pr[i]) {
            for (int j = i;j<1000;j+=i) {
                pr[j] = false;
            }
            cur *= i;
        }
        prod *= (m / cur % MOD);
        prod %= MOD;
        // cout << i << " " << prod << endl;
        if (!prod) break;
        
        tot = (tot - prod + MOD) % MOD; 
    }

    cout << tot << endl;

    return 0;
}
#include <bits/stdc++.h>

using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> k;
        vi val(k), ret(k, 0), diff(k, 0);
        int sm = 0, acc = 0;
        for (int i = 0;i < k;i++) {
            cin >> val[i];
            sm += val[i];
        }
        for (int i = k-1;i >= 0;i--) {
            int amt = sm / (i+1);
            cout << i << " " << amt << " " << (sm % (i+1)) << endl;
            if (!amt) break;
            acc += diff[i];
            val[i] += acc;
            val[i] -= k-i;
            if (i >= amt) diff[i-amt]++;
            sm -= val[i];
            ret[i] = val[i] ? 1 : 0;
        }
        for (auto x:ret) {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}
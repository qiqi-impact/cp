#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vector<int>>;

bool solve() {

    int k;
    cin >> k;
    vector<ll> amt(k);

    ll tot = 0;
    for (int i = 0;i < k;i++) {
        cin >> amt[i];
        tot += amt[i];
    }

    auto comp = [&](int a, int b) {
        return amt[a] < amt[b];
    };

    ll sm = 0;
    vector<ll> fib;
    while (1) {
        if (fib.size() < 2) {
            fib.push_back(1);
            sm++;
        } else {
            fib.push_back(fib[fib.size()-2] + fib[fib.size()-1]);
            sm += fib.back();
        }
        if (sm == tot) break;
        if (sm > tot) return false;
    }

    priority_queue<int, vector<int>, decltype(comp)> h(comp);

    for (int i = 0;i < k;i++) h.push(i);

    int lst = -1;
    for (int i = fib.size()-1;i >= 0;i--) {
        int later = -1;
        if (h.top() == lst) {
            later = lst;
            h.pop();
            if (h.empty()) return false;
        }
        lst = h.top();
        h.pop();
        if (amt[lst] < fib[i]) return false;
        amt[lst] -= fib[i];
        tot -= fib[i];
        h.push(lst);
        if (later != -1) h.push(later);
    }
    
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) cout << (solve() ? "YES" : "NO") << endl;
}
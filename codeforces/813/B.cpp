#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
 
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vi v(n);
        bool down = true;
        for (int i = n-1;i >= 0;i--) {
            if (down) v[i] = i; else v[i] = i+2;
            down = !down;
        }
        for (auto x: v) cout << max(1, x) << " ";
        cout << endl;
    }
    return 0;
}
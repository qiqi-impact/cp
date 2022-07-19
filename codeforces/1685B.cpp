#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

void solve() {
    vi cts(4, 0);
    string s;
    for (int i = 0;i < 4;i++) cin >> cts[i];
    cin >> s;
    int cta = 0, ctb = 0;

    vi aruns, bruns;
    int flextiles = 0;

    for (int i = 0;i < s.length();i++) {
        if (s[i] == 'A') {
            cta++;
        } else {
            ctb++;
        }
    }
    if (cts[0] + cts[2] + cts[3] != cta || cts[1] + cts[2] + cts[3] != ctb) {
        cout << "NO" << endl;
        return;
    }
    cta = ctb = 0;

    int crun = 0;
    char ch = 0;
    for (int i = 0;i < s.length();i++) {
        if (s[i] == 'A') {
            cta++;
            if (!ch || ch == 'B') {
                crun++;
            } else if (crun%2) {
                // cout << crun << endl;
                flextiles += crun/2;
                cts[0] -= 1;
                crun = 1;
            } else {
                // cout << crun << endl;
                bruns.push_back(crun/2);
                crun = 1;
            }
        } else {
            ctb++;
            if (!ch || ch == 'A') {
                crun++;
            } else if (crun%2) {
                // cout << crun << endl;
                flextiles += crun/2;
                cts[1] -= 1;
                crun = 1;
            } else {
                // cout << crun << endl;
                aruns.push_back(crun/2);
                crun = 1;
            }
        }
        ch = s[i];
    }

    if (ch == 'A') {
        if (crun%2) {
            // cout << crun << endl;
            flextiles += crun/2;
            cts[0] -= 1;
            crun = 1;
        } else {
            // cout << crun << endl;
            bruns.push_back(crun/2);
            crun = 1;
        }
    } else {
        if (crun%2) {
            // cout << crun << endl;
            flextiles += crun/2;
            cts[1] -= 1;
            crun = 1;
        } else {
            // cout << crun << endl;
            aruns.push_back(crun/2);
            crun = 1;
        }
    }

    sort(aruns.begin(), aruns.end());
    sort(bruns.begin(), bruns.end());

    // for (auto x : aruns) {
    //     cout << x << " ";
    // }
    // cout << endl;

    // for (auto x : bruns) {
    //     cout << x << " ";
    // }
    // cout << endl;

    // for (auto x : cts) {
    //     cout << x << " ";
    // }
    // cout << endl;

    // cout << flextiles << endl;

    
    int ataken = 0;
    while (ataken < aruns.size()) {
        int k = aruns[ataken];
        if (cts[2] >= k) {
            cts[2] -= k;
            ataken++;
        } else {
            break;
        }
    }
    cts[0] -= aruns.size() - ataken;
    cts[1] -= aruns.size() - ataken;
    int btaken = 0;
    while (btaken < bruns.size()) {
        int k = bruns[btaken];
        if (cts[3] >= k) {
            cts[3] -= k;
            btaken++;
        } else {
            break;
        }
    }
    cts[0] -= bruns.size() - btaken;
    cts[1] -= bruns.size() - btaken;
    if (cts[0] >= 0 && cts[1] >= 0) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
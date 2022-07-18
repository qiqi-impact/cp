#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int main() {
    vi primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
    int i = 0;
    int ct = 0;
    int mx = 100;
    int q = 0;
    string k;
    for (int i = 0;i < primes.size();i++) {
        if (primes[i] > mx) {
            break;
        }
        q++;
        cout << primes[i] << endl << flush;
        cin >> k;
        if (q == 20) break;
        if (k == "yes") {
            ct++;
            q++;
            if (ct == 2) break;
            mx /= primes[i];
            if (primes[i] * primes[i] <= 100) {
                cout << primes[i] * primes[i] << endl << flush;
                cin >> k;
                if (k == "yes") {
                    ct++;
                    if (ct == 2) break;
                }
            }
            if (q == 20) break;
        }
    }
    if (ct == 2) cout << "composite"; else cout << "prime";
    cout << endl << flush;
    return 0;
}
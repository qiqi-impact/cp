#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int main() {
    vi primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
    int i = 0;
    int ct = 0;
    int mx = 50;
    string k;
    for (int i = 0;i < primes.size();i++) {
        cout << primes[i] << endl << flush;
        cin >> k;
        if (k == "yes") ct++;
    }
    for (int i = 0;i < 4;i++) {
        cout << primes[i]*primes[i] << endl << flush;
        cin >> k;
        if (k == "yes") ct++;
    }
    if (ct >= 2) cout << "composite"; else cout << "prime";
    cout << endl << flush;
    return 0;
}
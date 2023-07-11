#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

string complement(string a, string b) {
    string ret;
    for (int i = 0;i < a.size();i++) {
        if (a[i] != b[i]) {
            ret += (3 - (a[i]-'0') - (b[i]-'0')) + '0';
        } else {
            ret += a[i];
        }
    }
    return ret;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<string> cards(n);
    unordered_set<string> sc;
    unordered_map<string, int> wings;
    for (int i = 0;i < n;i++) {
        for (int j = 0;j < k;j++) {
            char c;
            cin >> c;
            cards[i] += c;
        }
        sc.insert(cards[i]);
    }
    
    for (auto &s : cards) {
        for (auto &t : cards) {
            if (s == t) continue;
            string u = complement(s, t);
            if (sc.count(u)) {
                wings[s]++;
            }
        }
    }

    ll ret = 0;
    for (auto &[a, b] : wings) {
        ret += b * (b - 2) / 8;
    }
    cout << ret << endl;
    return 0;
}
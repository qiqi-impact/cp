#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int comp(char a, char b) {
    if (a < b) return 1;
    else if (a > b) return -1;
    return 0;
}

const int MX = 2222;
int dp[MX][MX];

int eval(string &s, int l, int r) {
    if (l > r) return 0;

    if (dp[l][r] != 2) return dp[l][r];
    
    int ret = -1;

    // alice has picked left
    int bl = eval(s, l+2, r);
    int br = eval(s, l+1, r-1);

    if (!bl) bl = comp(s[l], s[l+1]);
    if (!br) br = comp(s[l], s[r]);

    ret = max(ret, min(bl, br));

    // alice has picked right
    bl = eval(s, l+1, r-1);
    br = eval(s, l, r-2);

    if (!bl) bl = comp(s[r], s[l]);
    if (!br) br = comp(s[r], s[r-1]);

    ret = max(ret, min(bl, br));
    dp[l][r] = ret;
    return ret;
}


int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        for (int i = 0;i < s.size();i++) {
            for (int j = 0;j < s.size();j++) {
                dp[i][j] = 2;
            }
        }
        int v = eval(s, 0, s.size() - 1);
        if (v == 0) cout << "Draw";
        if (v == 1) cout << "Alice";
        if (v == -1) cout << "Bob";
        cout << endl;
    }
    return 0;
}
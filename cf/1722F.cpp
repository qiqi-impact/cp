#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;

bool neighbor(vvi &b, int x, int y) {
    for (int i = x-1;i <= x+1;i++) {
        for (int j = y-1;j <= y+1;j++) {
            if (i >= 0 && i < b.size() && j >= 0 && j < b[i].size() && b[i][j] == 1) {
                return false;
            }
        }
    }
    return true;
}

bool solve() {
    int r, c;
    cin >> r >> c;
    vvi b(r, vi(c));
    for (int i = 0;i < r;i++) {
        string s;
        cin >> s;
        for (int j = 0;j < c;j++) {
            b[i][j] = (int)(s[j] == '*');
        }
    }
    for (int i = 0;i < r;i++) {
        for (int j = 0;j < c;j++) {
            if (!b[i][j]) continue;

            int up = i > 0 && b[i-1][j] == 1;
            int left = j > 0 && b[i][j-1] == 1;
            int down = i < r-1 && b[i+1][j] == 1;
            int right = j < c-1 && b[i][j+1] == 1;
            if ((up && down) || (left && right)) return false;

            if (up && left) {
                b[i][j] = 0;
                b[i-1][j] = 0;
                b[i][j-1] = 0;
                if (!neighbor(b, i, j)) return false;
                if (!neighbor(b, i-1, j)) return false;
                if (!neighbor(b, i, j-1)) return false;
            } else if (up && right) {
                b[i][j] = 0;
                b[i-1][j] = 0;
                b[i][j+1] = 0;
                if (!neighbor(b, i, j)) return false;
                if (!neighbor(b, i-1, j)) return false;
                if (!neighbor(b, i, j+1)) return false;
            } else if (down && left) {
                b[i][j] = 0;
                b[i+1][j] = 0;
                b[i][j-1] = 0;
                if (!neighbor(b, i, j)) return false;
                if (!neighbor(b, i+1, j)) return false;
                if (!neighbor(b, i, j-1)) return false;
            } else if (down && right) {
                b[i][j] = 0;
                b[i+1][j] = 0;
                b[i][j+1] = 0;
                if (!neighbor(b, i, j)) return false;
                if (!neighbor(b, i+1, j)) return false;
                if (!neighbor(b, i, j+1)) return false;
            }
        }
    }

    for (int i = 0;i < r;i++) {
        for (int j = 0;j < c;j++) {
            if (b[i][j]) return false;
        }
    }
    return true;
    
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << (solve() ? "YES" : "NO") << endl;
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int m, n;
        cin >> m >> n;
        vvi in(m, vi(n));

        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++) {
                char c;
                cin >> c;
                in[i][j] = c - '0';
            }

        vvi left(m, vi(n, 0));
        vvi up(m, vi(n, 0));
        vvi rect(m, vi(n, 0));
        for (int i = 0;i < m;i++)
            for (int j = 0;j < n;j++) {
                left[i][j] = in[i][j];
                if (j != 0) left[i][j] += left[i][j-1];
                up[i][j] = in[i][j];
                if (i != 0) up[i][j] += up[i-1][j];
                rect[i][j] = in[i][j];
                if (i != 0) rect[i][j] += rect[i-1][j];
                if (j != 0) rect[i][j] += rect[i][j-1];
                if (i != 0 && j != 0) rect[i][j] -= rect[i-1][j-1];
                // cout << i << " " << j << " " << left[i][j] << " " << up[i][j] << " " << rect[i][j] << endl;
            }

        int mn = m*n;
        for (int i = 4;i < m;i++) {
            for (int j = 3;j < n;j++) {
                for (int a = 0;a <= i-4;a++) {
                    for (int b = 0;b <= j-3;b++) {
                        int sides = left[i][j-1] + left[a][j-1] + up[i-1][j] + up[i-1][b];
                        sides -= left[i][b] + left[a][b];
                        sides -= up[a][j] + up[a][b];
                        int mid = rect[i-1][j-1] - rect[a][j-1] - rect[i-1][b] + rect[a][b];
                        // cout << i << " " << j << " " << a << " " << b << " " << sides << " " << mid << endl;
                        mn = min(mn, 2 * (i - a - 1 + j - b - 1) - sides + mid);
                    }
                }
            }
        }
        cout << mn << endl;
        return 0;
    }
}
/*

 xxx
x  
x  
x  
 xxx

*/
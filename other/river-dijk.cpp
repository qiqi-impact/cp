#include <bits/stdc++.h>
using namespace std;

int DIR[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

int main() {
    int n, m;
    cin >> n >> m;
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    vector<string> board(n);
    for (int i = 0;i < n;i++) {
        cin >> board[i];
    }
    vector<vector<int>> cost(n, vector<int>(m, INT_MAX));
    cost[a][b] = 0;
    priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
    pq.push({0,a,b});
    while (!pq.empty()) {
        vector<int> v = pq.top();
        pq.pop();
        if (v[1] == c && v[2] == d) {
            cout << v[0] << endl;
            return 0;
        }
        if (cost[v[1]][v[2]] != v[0]) continue;
        for (auto &[dx, dy] : DIR) {
            int nx = v[1] + dx;
            int ny = v[2] + dy;
            if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] != '#') {
                int new_cost = v[0] + int(nx < v[1]) + int(ny < v[2]);
                if (new_cost < cost[nx][ny]) {
                    cost[nx][ny] = new_cost;
                    pq.push({new_cost, nx, ny});
                }
            }
        }
    }
    cout << -1 << endl;
    return 0;
}
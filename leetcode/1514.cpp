#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;
using vvi = vector<vector<int>>;
using pfi = pair<double, int>;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        vector<unordered_map<int, double>> g(n);
        for (int i = 0;i < edges.size();i++) {
            int x = edges[i][0];
            int y = edges[i][1];
            g[x][y] = g[y][x] = succProb[i];
        }
        priority_queue<pfi, vector<pfi>> pq;
        pq.emplace(1.0, start);
        vector<double> prob(n, 0);
        prob[start] = 1.0;
        while (!pq.empty()) {
            auto [p, idx] = pq.top();
            // cout << p << " " << idx << endl;
            pq.pop();
            if (idx == end) return p;
            if (p < prob[idx]) continue;
            for (auto &[other, val] : g[idx]) {
                if (val * prob[idx] > prob[other]) {
                    prob[other] = val * prob[idx];
                    pq.emplace(val * prob[idx], other);
                }
            }
        }
        return 0;
    }
};
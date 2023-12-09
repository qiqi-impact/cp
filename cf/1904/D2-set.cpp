#include <bits/stdc++.h>
using namespace std;

#define MAXN 200005

int NT, N, A[MAXN], B[MAXN];
bool R[MAXN];
set<int> S;

bool sol() {
    S = {};
    for (int i = 0; i < N; ++i) {
        R[i] |= A[i] == B[i] || S.find(B[i]) != S.end();
        S.erase(begin(S), S.lower_bound(A[i]));
        S.erase(S.upper_bound(B[i]), end(S));
        S.insert(A[i]);
    }
    S = {};
    for (int i = N-1; i >= 0; --i) {
        R[i] |= A[i] == B[i] || S.find(B[i]) != S.end();
        S.erase(begin(S), S.lower_bound(A[i]));
        S.erase(S.upper_bound(B[i]), end(S));
        S.insert(A[i]);
    }
    for (int i = 0; i < N; ++i) {
        if (!R[i]) return 0;
    }
    return 1;
}

int main() {
    cin >> NT;
    while (NT--) {
        cin >> N;
        for (int i = 0; i < N; ++i) cin >> A[i];
        for (int i = 0; i < N; ++i) cin >> B[i];
        for (int i = 0; i < N; ++i) R[i] = 0;
        cout << (sol() ? "YES" : "NO") << endl;
    }
}
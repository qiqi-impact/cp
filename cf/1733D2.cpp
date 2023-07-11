#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;

ll solve() {
	int n;
	ll x, y;
	cin >> n >> x >> y;
	vi ab(n, 0);
	string s;
	cin >> s;
	for (int i = 0;i < n;i++) ab[i] ^= (int)(s[i] - '0');
	cin >> s;
	vi ind;
	for (int i = 0;i < n;i++) {
		ab[i] ^= (int)(s[i] - '0');
		if (ab[i]) ind.push_back(i);
	}
	int is = ind.size();
	if (is%2) return -1;
	if (is == 0) return 0;
	if (is == 2 && ind[1] == ind[0] + 1) {
		if (n == 2) return x;
		return min(x, 2 * y);
	}
	vector<ll> dp(1+is, 0);
	dp[is-1] = y;
	for (int i = is-2;i >= 0;i--) {
		dp[i] = min(2 * x * (ind[i+1] - ind[i]) + dp[i+2], y + dp[i+1]);
	}
	return dp[0]/2;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		cout << solve() << endl;
	}
	return 0;
}
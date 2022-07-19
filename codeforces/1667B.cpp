#include <bits/stdc++.h>

using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int k;
		cin >> k;
		vi v(k), sm(k+1, 0), dp(k+1, -1e9);
		dp[k] = 0;
		set<pii> seen;
		for (int i = 0;i < k;i++) {
			cin >> v[i];
			sm[i+1] = sm[i] + v[i];
		}

		// for (auto x : sm) {
		// 	cout << x << " ";
		// }
		// cout << endl;

		int ret = -1e9;
		seen.insert(pii(sm[k], -k));
		for (int i = k-1;i >= 0;i--) {
			auto it = seen.upper_bound(pii(sm[i]+1, -1e9));
			// cout << i << " " << (int)(it == seen.end()) << endl;
			int cur = 0;
			if (v[i] > 0) cur = 1;
			if (v[i] < 0) cur = -1;
			dp[i] = cur + dp[i+1];
			if (it != seen.end()) {
				pii x = *it;
				int idx = -x.second;
				int val = x.first;
				dp[i] = max(dp[i], dp[idx] + (idx - i));
			}
			// ret = max(ret, dp[i]);
			seen.insert(pii(sm[i], -i));
		}
		// for (auto x : dp) {
		// 	cout << x << " ";
		// }
		// cout << endl;
		cout << dp[0] << endl;
	}
	return 0;
}
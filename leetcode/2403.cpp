class Solution {
public:
    long long minimumTime(vector<int>& power) {
        int n = power.size();
        vector<long long> dp(1 << n, (long long)1e18);
        dp[(1 << n) - 1] = 0;
        for (int i = (1 << n)-2;i >= 0;i--) {
            int m = 1 + __builtin_popcount(i);
            for (int j = 0;j < n;j++) {
                if ((i & (1 << j)) == 0) {
                    dp[i] = min(dp[i], dp[i ^ (1 << j)] + (power[j] + m - 1) / m);
                }
            }
        }
        return dp[0];
    }
};
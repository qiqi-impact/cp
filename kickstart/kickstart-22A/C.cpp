#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int> > vv32;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define forsn(i,s,e) for(ll i = s; i < e; i++)
#define rforn(i,s) for(ll i = s; i >= 0; i--)
#define rforsn(i,s,e) for(ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout<<#x<<" = "<<x<<ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())

unordered_set<int> valid5, valid6;

void solve() {
    string s;
    int t;
    cin >> t >> s;
    unordered_set<int> ov;
    ov.insert(0);
    forn(i, s.length()) {
        unordered_set<int> nv;
        v32 opt;
        if (s[i] == '0' || s[i] == '?') opt.pb(0);
        if (s[i] == '1' || s[i] == '?') opt.pb(1);
        for(auto x : ov) {
            for (auto y : opt) {
                if ((i < 5 || valid6.find(2*x + y) != valid6.end()) &&
                    (i < 4 || valid5.find((2*x + y)%32) != valid5.end())) {
                    nv.insert((2*x + y)%32);
                    // cout << (2*x + y)%32 << " ";
                }
            }
        }
        // cout << endl;
        if (nv.empty()) {
            cout << "IMPOSSIBLE";
            return;
        }
        ov = nv;
    }
    cout << "POSSIBLE";
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

    forn(i, 64) {
        bool p = true;
        forn(j, 3) {
            ll k = 5-j;
            if ((i>>j & 1) != (i>>k & 1)) {
                p = false;
                break;
            }
        }
        if (!p) {
            valid6.insert(i);
            // cout << i << " ";
        }
    }
    // cout << endl;

    forn(i, 32) {
        bool p = true;
        forn(j, 2) {
            ll k = 4-j;
            if ((i>>j & 1) != (i>>k & 1)) {
                p = false;
                break;
            }
        }
        if (!p) {
            valid5.insert(i);
            // cout << i << " ";
        }
    }
    // cout << endl;

	fast_cin();
	ll t;
	cin >> t;
    forn(i, t) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
	return 0;
}

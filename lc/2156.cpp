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

string subStrHash(string s, int power, int modulo, int k, int hashValue) {
    ll pp = 1;
    ll cur = 0;
    ll sl = s.length();
    for (int i = 0;i < k;i++) {
        pp *= power;
        pp %= modulo;
    }
    int ret = -1;
    for (int i = sl-1;i >= 0;i--) {
        cur = cur * power + s[i]-'a'+1;
        cur %= modulo;
        if (i <= sl-k-1) {
            cur -= (s[i+k]-'a'+1) * pp;
            cur = ((cur % modulo) + modulo) % modulo;
        }
        if (i <= sl-k && cur == hashValue) {
            ret = i;
        }
    }
    if (ret == -1) return "-1";
    return s.substr(ret, k);
}

int main() {
    fast_cin();
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    string s;
    int power, modulo, k, hashValue;
    cin >> s >> power >> modulo >> k >> hashValue;
    cout << subStrHash(s, power, modulo, k, hashValue) << endl;
    return 0;
}
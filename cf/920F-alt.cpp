#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <limits.h>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <time.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>
 
#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:336777216")
using namespace std;
 
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define ldb ldouble
 
typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;
 
int IT_MAX = 1 << 19;
ll MOD = 1000000007;
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;
const db PI = acos(-1);
const db ERR = 1e-10;
#define szz(x) (int)(x).size()
#define rep(i, n) for(int i=0;i<n;i++)
#define Se second
#define Fi first
 
ll indt[1100000];
void update(int p, ll v) {
	p += IT_MAX - 1;
	indt[p] = v;
	for (p /= 2; p; p /= 2) indt[p] = indt[2 * p] + indt[2 * p + 1];
}
ll getsum(int p1, int p2) {
	p1 += IT_MAX - 1;
	p2 += IT_MAX - 1;
	ll rv = 0;
	for (; p1 <= p2; p1 /= 2, p2 /= 2) {
		if (p1 % 2 == 1) rv = rv + indt[p1++];
		if (p2 % 2 == 0) rv = rv + indt[p2--];
	}
	return rv;
}
 
set <int> Sx;
int in[300050];
int D[1000050];
 
vector <int> Vl;
int main() {
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N, M, i, j;
	scanf("%d %d", &N, &M);
	for (i = 1; i <= N; i++) scanf("%d", &in[i]);
	for (i = 1; i <= N; i++) update(i, in[i]);
	for (i = 1; i <= N; i++) if (in[i] >= 3) Sx.insert(i);
 
	for (i = 1; i <= 1000000; i++) for (j = i; j <= 1000000; j += i) D[j]++;
	while (M--) {
		int t1, t2, t3;
		scanf("%d %d %d", &t1, &t2, &t3);
		if (t1 == 1) {
			while (1) {
				auto it = Sx.lower_bound(t2);
				if (it == Sx.end() || *it > t3) break;
				Vl.push_back(*it);
				Sx.erase(it);
			}
			for (auto it : Vl) {
				in[it] = D[in[it]];
				update(it, in[it]);
				if (in[it] >= 3) Sx.insert(it);
			}
			Vl.clear();
		}
		else printf("%lld\n", getsum(t2, t3));
	}
	return 0;
}
//*/
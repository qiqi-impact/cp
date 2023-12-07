#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
using vi = vector<int>;
using vvi = vector<vi>;
using vll = vector<ll>;
using vvll = vector<vll>;
using pii = pair<int, int>;

namespace output {
	void pr(int x) { cout << x; }
	void pr(long x) { cout << x; }
	void pr(ll x) { cout << x; }
	void pr(unsigned x) { cout << x; }
	void pr(unsigned long x) { cout << x; }
	void pr(unsigned long long x) { cout << x; }
	void pr(float x) { cout << x; }
	void pr(double x) { cout << x; }
	void pr(ld x) { cout << x; }
	void pr(char x) { cout << x; }
	void pr(const char* x) { cout << x; }
	void pr(const string& x) { cout << x; }
	void pr(bool x) { pr(x ? "true" : "false"); }
	template<class T> void pr(const complex<T>& x) { cout << x; }
	
	template<class T1, class T2> void pr(const pair<T1,T2>& x);
	template<class T> void pr(const T& x);
	
	template<class T, class... Ts> void pr(const T& t, const Ts&... ts) { 
		pr(t); pr(ts...); 
	}
	template<class T1, class T2> void pr(const pair<T1,T2>& x) { 
		pr("{",x.first,", ",x.second,"}"); 
	}
	template<class T> void pr(const T& x) { 
		pr("{"); // const iterator needed for vector<bool>
		bool fst = 1; for (const auto& a: x) pr(!fst?", ":"",a), fst = 0; 
		pr("}");
	}
	
	void ps() { pr("\n"); } // print w/ spaces
	template<class T, class... Ts> void ps(const T& t, const Ts&... ts) { 
		pr(t); if (sizeof...(ts)) pr(" "); ps(ts...); 
	}
	
	void pc() { pr("]\n"); } // debug w/ commas
	template<class T, class... Ts> void pc(const T& t, const Ts&... ts) { 
		pr(t); if (sizeof...(ts)) pr(", "); pc(ts...); 
	}
	#define dbg(x...) pr("[",#x,"] = ["), pc(x);
}

using namespace output;

/*
    pair = start/end
*/
vector<vector<long long>> merge(vector<vector<long long>> intervals) {
    vector<pair<long long, long long>> events;
    vector<vector<long long>> result;
    for(auto& i : intervals) {
        events.push_back({i[0], 0});
        events.push_back({i[1], 1});
    }

    sort(events.begin(), events.end());

    stack<pair<long long, long long>> stk;
    for(auto& e : events) {
        if(e.second == 0) stk.push(e);
        else if(e.second == 1 && stk.size() == 1) {
            result.push_back({stk.top().first, e.first});
            stk.pop();
        }
        else if(e.second == 1) stk.pop();
    }
    return result;

}

vector<vector<long long>> split(vector<vector<long long>> seeds, vector<vector<long long>> maps) {
    vvll cur(seeds.begin(), seeds.end());
    for(int j = 0; j < maps.size(); j++) {
        vvll nc;
        ll c = maps[j][1];
        ll d = maps[j][1] + maps[j][2] - 1;
        for (auto x : cur) {
            ll a = x[0];
            ll b = x[1];
            if ((a >= c && b <= d) || c > b || a > d) {
                nc.push_back({a, b});
            } else if (a < c && b <= d) {
                nc.push_back({a, c-1});
                nc.push_back({c, b});
            } else if (a >= c && b > d) {
                nc.push_back({a, d});
                nc.push_back({d+1, b});
            } else {
                nc.push_back({a, c-1});
                nc.push_back({c, d});
                nc.push_back({d+1, b});
            }
        }
        cur = vvll(nc.begin(), nc.end());
        // dbg(1, cur);
    }
    return cur;
}

vector<vector<long long>> shiftI(vector<vector<long long>> seeds, vector<vector<long long>> maps) {
    vector<vector<long long>> result;
    for(int i = 0; i < seeds.size(); i++) {
        bool found = false;
        for(int j = 0; j < maps.size(); j++) {
            if(seeds[i][0] >= maps[j][1] && seeds[i][1] <= maps[j][1]+maps[j][2]-1) {
                found = true;
                long long delta = maps[j][0]-maps[j][1];
                result.push_back({seeds[i][0]+delta, seeds[i][1]+delta});
                break;
            }
        }
        if(!found) result.push_back(seeds[i]);
    }
    return result;
}
/*
seed-to-soil
1   10  20  30  40  50  60  70  80  90  100
                                        <>
                    <------------------>                 Direct shift
1   10  20  30  40  50  60  70  80  90  100
                                <----->
                       <--->
Direct shift 2
1   10  20  30  40  50  60  70  80  90  100
                                 <----->
                        <--->
*/

/*
soil-to-fertilizer
1   10  20  30  40  50  60  70  80  90  100
       <------------->
                     <>
<------>                                                 No Overlap
No Overlap
1   10  20  30  40  50  60  70  80  90  100
                                 <----->
                        <--->
*/

/*
fertilizer-to-water
1   10  20  30  40  50  60  70  80  90  100
                     <--->
     <--------------->
<-->
   <->
split on 57-60                                           Split
1   10  20  30  40  50  60  70  80  90  100
                                 <----->
                        <--->
1   10  20  30  40  50  60  70  80  90  100
                                 <----->
                        <>
                         <-->
1   10  20  30  40  50  60  70  80  90  100
                                 <----->
                     <>
                         <-->

PAIRS {81, 94} {57, 69}->{57, 60}{61, 69} split
      {81, 94} {53, 65} {61, 69} shift


merge where can be merged
split based on map
direct shift ranges
*/

int main(int argc, char* argv[]) {
    if(argc != 2) return 0;
    string fname = argv[1];
    ifstream ifs(fname);
    if(ifs.is_open()) {
        string line = "";
        vector<long long> seeds;
        unordered_map<string, vector<vector<long long>>> maps;
        while(getline(ifs, line)) {
            if(line == "") continue;
            stringstream ss(line);
            string buffer = "";
            ss >> buffer;
            if(buffer == "seeds:") {
                while(ss >> buffer) {
                    seeds.push_back(stoll(buffer));
                }
            }
            else {
                while(getline(ifs, line)) {
                    if(line == "") break;
                    stringstream SS(line);
                    string buffer1 = "";
                    string something = "";
                    SS >> something;
                    long long dest = stoll(something);
                    SS >> something;
                    long long src = stoll(something);
                    SS >> something;
                    long long rng = stoll(something);
                    maps[buffer].push_back({dest, src, rng});
                }
            }
        }
        long long lowest = 10e9+7;
        vector<string> types = {"seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"};
        vector<vector<long long>> intervals;
        for(int i = 0; i < seeds.size(); i+=2) {
            intervals.push_back({seeds[i], seeds[i]+seeds[i+1]-1});
        }
        dbg(intervals);

        for(auto& t : types) {
            // dbg(maps[t]);
            intervals = merge(intervals);
            // dbg(intervals);
            intervals = split(intervals, maps[t]);
            // dbg(intervals);
            intervals = shiftI(intervals, maps[t]);
            // dbg(intervals);
        }
        for(auto& i : intervals) {
            cout << i[0] << "," << i[1] << endl;
            lowest = min(lowest, i[0]);
        }
        cout << lowest << endl;
    }
    return 0;
}
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class KMP {
    string pattern;
    vector <int> fail;

    void initKMP(const string &p) {
        pattern = p;
        int m = pattern.size();
        fail.assign(m + 1, -1);
        for (int i = 0, j = -1; i < m; i++) {
            while (j >= 0 && pattern[i] != pattern[j]) j = fail[j];
            j++;
            if (pattern[i + 1] == pattern[j]) fail[i + 1] = fail[j];
            else fail[i + 1] = j;
        }
    }

    void initMP(const string &p) {
        pattern = p;
        int m = pattern.size();
        fail.assign(m + 1, -1);
        for (int i = 0, j = -1; i < m; i++) {
            while (j >= 0 && pattern[i] != pattern[j]) j = fail[j];
            fail[i+1] = ++j;
        }
    }

public:
    KMP(const string &p) { initKMP(p); }

    int period(int i) { return i - fail[i]; }

    vector <int> match(const string &s) {
        int n = s.size();
        int m = pattern.size();
        vector <int> res;
        for (int i = 0, k = 0; i < n; i++) {
            while (k >= 0 && s[i] != pattern[k]) k = fail[k];
            k++;
            if (k == m) res.push_back(i - m + 1);
        }
        return res;
    }
};

int main() {
    string s = "abcdabc";
    string p = "abc";
    KMP kmp(p);
    vector <int> ans = kmp.match(s);
    for (int i : ans) cout << i << "\n";
}
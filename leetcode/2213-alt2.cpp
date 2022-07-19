#include <bits/stdc++.h>

using namespace std;

string s; 
// 单点修改 (不需要 Lazy)
struct Segment{
    int l, r; 
    int prefix, suffix, maxLen; 
};

Segment tree[400005]; 

void push_up(int i, int l, int r){
    Segment &lt = tree[2*i]; 
    Segment &rt = tree[2*i+1]; 
    // 当前节点的最长长度取决于左右
    tree[i].maxLen = std::max(lt.maxLen, rt.maxLen); 
    // 新的区间的 prefix 就是 左区间的 prefix 
    tree[i].prefix = lt.prefix; 
    // 新的区间的 suffix 就是 右区间的 suffix 
    tree[i].suffix = rt.suffix; 
    int m = ((l+r) >> 1); 
    // 如果能合并
    if (s[m] == s[m+1]){
        tree[i].maxLen = std::max(tree[i].maxLen, lt.suffix + rt.prefix); 
        if (lt.maxLen == m - l + 1){
            tree[i].prefix += rt.prefix; 
        }
        if (rt.maxLen == r - m){
            tree[i].suffix += lt.suffix; 
        }
    }

}

void build(int i, int l, int r){
    if (l == r){
        tree[i].l = l, tree[i].r = r; 
        tree[i].prefix = tree[i].suffix = tree[i].maxLen = 1; 
    }else{
        int m = ((l+r) >> 1); 
        build(2*i, l, m); 
        build(2*i+1, m+1, r); 
        push_up(i, l, r);  // 实际上 ans[i] = ans[2*i] + ans[2*i+1] 
    }    
}


int query(int i, int l, int r, int p, char c){
    if (l == r){
        s[l] = c; 
    }else{
        int m = (l + r) / 2; 
        // 修改的位置在左边
        if (p <= m) query(2*i, l, m, p, c); 
        // 修改的位置在右边
        else query(2*i+1, m+1, r, p, c); 
        // 走完下面的，就可以更新这一层了
        push_up(i, l, r); 
    }
    return tree[i].maxLen; 
}


class Solution {
public:
    vector<int> longestRepeating(string _s, string queryCharacters, vector<int>& queryIndices) {
        s = _s; 
        
        build(1, 0, s.size() - 1); 

        vector<int> ans; 
        for (int i = 0; i < queryCharacters.size(); i++){
            ans.push_back(query(1, 0, s.size() - 1, queryIndices[i], queryCharacters[i])); 
        }
        return ans; 
    }
};
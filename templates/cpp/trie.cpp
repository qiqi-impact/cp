// madflash19
// Usage:
// 
// trie t;
// t.add(..);
// 
// int root = 0;
// 
// if (t[root].has(your_child)) {
//    root = t[root][your_child];
// }

struct trie {
    struct node {
        array<int, 26> child;
        int eow = 0, cnt = 0;
        node() { fill(child.begin(), child.end(), -1); }
        inline bool has(int c) const { return child[c] != -1; }
        int operator[](int c) const { return child[c]; }
    };

    vector<node> nodes;

    trie() { alloc(); }

    int alloc() {
        nodes.push_back(node());
        return nodes.size() - 1;
    }

    void add(string word) {
        int now = 0;
        for (char ch : word) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                nodes[now].child[id] = alloc();
            ++nodes[now].cnt;
            now = nodes[now].child[id];
        }
        ++nodes[now].eow;
        ++nodes[now].cnt;
    }

    node *search(string word) {
        int now = 0;
        for (char ch : word) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                return nullptr;
            now = nodes[now].child[id];
        }
        return (!nodes[now].eow) ? nullptr : &nodes[now];
    }

    pair<node &, int> prefix(string pre) {
        int now = 0, len = 0;
        for (char ch : pre) {
            int id = ch - 'a';
            if (!nodes[now].has(id))
                return {nodes[now], len};
            now = nodes[now].child[id];
            ++len;
        }
        return {nodes[now], len};
    }

    node &operator[](int i) { return nodes[i]; }
};
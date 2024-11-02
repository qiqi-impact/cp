template <typename T>
struct triexor {
    struct node {
        int child[2];
        int cnt = 0;
        bool eow = false;
        node() {
            child[0] = -1;
            child[1] = -1;
        }
        inline bool has(int c) { return child[c] != -1; }
        int operator[](int c) const { return child[c]; }
    };

    static constexpr int BITS = sizeof(T) * 8;
    vector<node> nodes;

    triexor() { alloc(); }

    int alloc() {
        nodes.pb(node());
        return sz(nodes) - 1;
    }

    void add(T n) {
        int now = 0;
        for (int i = BITS - 1; i >= 0; --i) {
            ++nodes[now].cnt;
            int bit = (n >> i) & 1;
            if (!nodes[now].has(bit))
                nodes[now].child[bit] = alloc();
            now = nodes[now].child[bit];
        }
        nodes[now].eow = true;
        ++nodes[now].cnt;
    }

    void remove(T n) {
        int now = 0;
        for (int i = BITS - 1; i >= 0; --i) {
            --nodes[now].cnt;
            int bit = (n >> i) & 1;
            if (!nodes[now].has(bit))
                assert(false && "n must be present in trie");
            now = nodes[now].child[bit];
        }
        --nodes[now].cnt;
        if (!nodes[now].cnt)
            nodes[now].eow = false;
    }

    inline T max_xor(T n) { return kth_max_xor(n, 1); }

    T kth_max_xor(T n, int k) {
        int now = 0;
        T ret = 0;
        for (int i = BITS - 1; i >= 0 && now != -1; --i) {
            int bit = (n >> i) & 1;
            if (nodes[now].has(1 - bit) &&
                k <= nodes[nodes[now].child[1 - bit]].cnt) {
                ret |= T(1) << i;
                now = nodes[now].child[1 - bit];
            } else {
                if (nodes[now].has(1 - bit))
                    k -= nodes[nodes[now].child[1 - bit]].cnt;
                now = nodes[now].child[bit];
            }
        }
        return ret;
    }

    node &operator[](int i) { return nodes[i]; }
};
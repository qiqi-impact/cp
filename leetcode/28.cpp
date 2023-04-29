class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.length() < needle.length()) return -1;
        for (int i = 0;i < haystack.length() - needle.length() + 1;i++) {
            bool fail = false;
            for (int j = 0;j < needle.length();j++) {
                if (haystack[i+j] != needle[j]) {
                    fail = true;
                    break;
                }
            }
            if (!fail) return i;
        }
        return -1;
    }
};
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        bm = [0] * n
        for i in range(len(s)-1, -1, -1):
            bm[i] = 1 << (ord(s[i]) - 97)
            if i < n - 1:
                bm[i] |= bm[i+1]
        
        st = []
        for i, c in enumerate(s):
            if c not in st:
                while st and st[-1] > c and (bm[i] & (1 << (ord(st[-1]) - 97))):
                    st.pop()
                st.append(c)
        return ''.join(st)
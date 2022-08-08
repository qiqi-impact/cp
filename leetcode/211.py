class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
            if i == len(word)-1:
                cur['exists'] = True

    def search_helper(self, word: str, idx: int, node: dict) -> bool:
        if idx == len(word):
            return 'exists' in node
        c = word[idx]
        if c == '.':
            for k in node:
                if k != 'exists':
                    if self.search_helper(word, idx+1, node[k]):
                        return True
        else:
            if c in node:
                return self.search_helper(word, idx+1, node[c])
        return False
                
    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
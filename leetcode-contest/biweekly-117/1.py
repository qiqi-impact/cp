class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i in range(len(words)):
            if x in words[i]:
                ret.append(i)
        return ret
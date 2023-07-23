class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []
        for w in words:
            ret += w.split(separator)
        return [x for x in ret if x != '']
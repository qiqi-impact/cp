class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted([c for c in s]))
            d[ss].append(s)
        return list(d.values())
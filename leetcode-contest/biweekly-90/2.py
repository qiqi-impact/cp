class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        tot = set()
        for w in dictionary:
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    t = w[:i] + c + w[i+1:]
                    tot.add(t)
        
        def find(w):
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    t = w[:i] + c + w[i+1:]
                    if t in tot:
                        return True
        
        return [q for q in queries if find(q)]
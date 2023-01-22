class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        l = []
        for x, y in sorted(people, key=lambda x:(-x[0], x[1])):
            l.insert(y, [x, y])
        return l
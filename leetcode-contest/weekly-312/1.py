class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = list(zip(names, heights))
        l.sort(key=lambda x:x[1])
        return [x[0] for x in l][::-1]
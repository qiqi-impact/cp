class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def f(ni, d):
            if ni.isInteger():
                return ni.getInteger() * d
            else:
                return sum([f(x, d+1) for x in ni.getList()])
        
        return sum([f(x, 1) for x in nestedList])
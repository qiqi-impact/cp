class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        pop = defaultdict(int)
        vid = defaultdict(int)
        cv = defaultdict(set)
        idv = {}
        n = len(creators)
        mxpop = 0
        for i in range(n):
            pop[creators[i]] += views[i]
            vid[creators[i]] = max(vid[creators[i]], views[i])
            mxpop = max(mxpop, pop[creators[i]])
            cv[creators[i]].add(ids[i])
            if creators[i] not in idv:
                idv[creators[i]] = {}
            idv[creators[i]][ids[i]] = views[i]
        ret = []
        for k in pop:
            if pop[k] == mxpop:
                ret.append([k, None])
        for i in range(len(ret)):
            k = ret[i][0]
            mxv = -1
            mxid = None
            for idd in idv[k]:
                if idv[k][idd] > mxv or (idv[k][idd] == mxv and idd < mxid):
                    mxid = idd
                    mxv = idv[k][idd]
            ret[i][1] = mxid
        return ret
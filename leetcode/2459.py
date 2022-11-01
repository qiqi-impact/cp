class Solution:
    def sortArray(self, nums: List[int]) -> int:
        def swap(arr, tgt):
            pos = {}
            oop = set()
            for i, x in enumerate(arr):
                pos[x] = i
                if x != tgt[i]:
                    oop.add(x)
            ct = 0
            while oop:
                ct += 1
                if 0 in oop:
                    x = tgt[pos[0]]
                    arr[pos[0]], arr[pos[x]] = arr[pos[x]], arr[pos[0]]
                    pos[0], pos[x] = pos[x], pos[0]
                    if tgt[pos[0]] == 0:
                        oop.discard(0)
                    if tgt[pos[x]] == x:
                        oop.discard(x)
                else:
                    for q in oop:
                        break
                    arr[pos[0]], arr[pos[q]] = arr[pos[q]], arr[pos[0]]
                    pos[q], pos[0] = pos[0], pos[q]
                    oop.add(0)
            return ct
        n = len(nums)
        return min(swap(nums[:], list(range(n))), swap(nums, list(range(1, n)) + [0]))
class SegmentTree:
    def __init__(self, data, default=0, func=lambda x,y:x+y):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree([0] * n)
        for i in range(1, n-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                st[i] = 1
                # print(i)
        ret = []
        for x, y, z in queries:
            if x == 1:
                # print(y+1, z)
                ret.append(st.query(y+1, z))
            else:
                nums[y] = z
                for i in range(y-1, y+2):
                    if 1 <= i < n-1:
                        st[i] = int(nums[i] > nums[i-1] and nums[i] > nums[i+1])
        return ret
                        
        
        
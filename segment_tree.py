#using segment tree for efficiently answering range queries and updating data in a dataset.

class segmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def range_sum(self, l, r):
        res = 0  #res=result
        l += self.n   #l=left
        r += self.n   #r=right
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

data = [1,3,5,7,9,11]
seg_tree = segmentTree(data)
print(f"Range sum(1,4): {seg_tree.range_sum(1,4)}")
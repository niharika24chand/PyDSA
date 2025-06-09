#using segment tree for efficiently answering range queries and updating data in a dataset.

class segmentTree:
    def __init__(self, data):
        self.n = len(data) #Stores the size of the input data array.
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def range_sum(self, left, right):
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

data = [1,3,5,7,9,11]
seg_tree = segmentTree(data)
print(f"Range sum(1,4): {seg_tree.range_sum(1,4)}")
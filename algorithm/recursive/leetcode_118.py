class Solution:
    res = []

    # 生成第 row 行的数据
    def search(self, row, all_rows):
        if row == all_rows:
            return
        arr = [1] * (row + 1)
        for i in range(1, row):
            arr[i] = self.res[row - 1][i - 1] + self.res[row - 1][i]
        self.res.append(arr)
        self.search(row + 1, all_rows)

    def generate(self, numRows):
        self.res.clear()

        self.search(0, numRows)

        return self.res

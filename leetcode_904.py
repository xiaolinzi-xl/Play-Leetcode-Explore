class Solution:
    def totalFruit(self, tree):
        res = 1
        l, r = 0, 1
        n = len(tree)
        record = []
        record.append(tree[0])
        tmp_ans = 1
        index = -1
        flag = False  # 是否交叉，默认没有交叉
        while r < n:
            if tree[r] in record:
                tmp_ans += 1
                res = max(res, tmp_ans)
                if len(record) == 2 and tree[r] == record[0]:
                    flag = True
                r += 1
            elif len(record) == 1:
                record.append(tree[r])
                index = r
                r += 1
                tmp_ans += 1
                res = max(res, tmp_ans)
            else:
                if flag:
                    l = r - 1
                    element = tree[r - 1]
                    while tree[l] == element:
                        l -= 1
                    l += 1
                else:
                    l = index
                record.clear()
                record.append(tree[l])
                tmp_ans = r - l
                flag = False
        return res


if __name__ == '__main__':
    tree = [1, 2, 1]
    print(Solution().totalFruit(tree))

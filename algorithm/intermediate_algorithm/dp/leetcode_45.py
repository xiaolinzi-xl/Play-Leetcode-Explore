class Solution:
    # 超时
    def jump_1(self, nums):
        n = len(nums)
        dp = [2 << 63] * (n)
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            step = min(i + nums[i], n - 1)
            if step == n - 1:
                dp[i] = 1
                continue
            for j in range(step, i, -1):
                if dp[j] != 2 << 63:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]

    def jump(self, nums):
        n = len(nums)
        last_pos = n - 1
        pos_index = [n - 1]
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
                pos_index.append(i)
        pos_index = pos_index[::-1]
        print(pos_index)
        dp = [0] * len(pos_index)
        # for i in range
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))

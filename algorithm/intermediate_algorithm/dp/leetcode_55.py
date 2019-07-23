class Solution:
    dp = []

    def search(self, nums, idx):
        if self.dp[idx] != -1:
            return self.dp[idx]
        if nums[idx] + idx >= len(nums) - 1:
            self.dp[idx] = nums[idx] + idx
            return self.dp[idx]
        for step in range(1, nums[idx] + 1):
            self.dp[idx] = max(self.dp[idx], idx + step)
            if self.dp[idx] >= len(nums) - 1:
                break
            self.dp[idx] = max(self.dp[idx], self.search(nums, idx + step))
        return self.dp[idx]

    # 超时 递归版本
    def canJump_2(self, nums):
        self.dp = [-1] * len(nums)
        return self.search(nums, 0) >= len(nums) - 1

    # 超时 时间复杂度为O(n^2)，空间复杂度为O(n)
    def canJump_1(self, nums):
        n = len(nums)
        if n == 1:
            return True
        dp = [-1] * n
        dp[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            for j in range(min(i + nums[i], n - 1), i, -1):
                dp[i] = max(dp[i], dp[j])
                if dp[i] == n - 1:
                    break
            if dp[i] == n - 1 and nums[0] >= i:
                dp[0] = n - 1
                break
        return dp[0] == n - 1

    # 通过 贪心策略 时间复杂度为O(n)，空间复杂度为O(1)
    def canJump(self, nums):
        n = len(nums)
        last_pos = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump_1(nums))

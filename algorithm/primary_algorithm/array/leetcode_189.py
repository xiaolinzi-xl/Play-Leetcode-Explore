class Solution:

    # 时间复杂度 O(N)，空间复杂度为 O(k)
    def rotate_1(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        arr = nums[n - k:]
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = arr[i]

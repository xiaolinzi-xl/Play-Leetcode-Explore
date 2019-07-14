class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        # [0,k] 保存不重复元素
        k = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[k]:
                nums[k + 1] = nums[i]
                k += 1
        return k + 1

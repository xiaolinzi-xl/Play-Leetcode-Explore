class Solution:
    def singleNumber(self, nums):
        if len(nums) == 0:
            return nums[0]
        ans = nums[0] ^ nums[1]
        for i in range(2, len(nums)):
            ans ^= nums[i]
        return ans

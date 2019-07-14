class Solution:
    def containsDuplicate(self, nums):
        duplicate = set()
        for ele in nums:
            if ele in duplicate:
                return True
            duplicate.add(ele)
        return False

class Solution:

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # 采用双指针，O(1) 的空间复杂度，O(n) 的时间复杂度
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy_arr = nums1[:m]
        i, j = 0, 0
        for k in range(m + n):
            if i >= m:
                nums1[k] = nums2[j]
                j += 1
            elif j >= n:
                nums1[k] = copy_arr[i]
                i += 1
            elif copy_arr[i] <= nums2[j]:
                nums1[k] = copy_arr[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

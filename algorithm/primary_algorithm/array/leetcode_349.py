class Solution:
    def intersect(self, nums1, nums2):
        map = {}
        for ele in nums1:
            if ele in map:
                map[ele] += 1
            else:
                map[ele] = 1
        ans = []
        for ele in nums2:
            if ele in map and map[ele] >= 1:
                ans.append(ele)
                map[ele] -= 1
        return ans

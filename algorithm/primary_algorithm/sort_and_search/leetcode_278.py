# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        # If nums1 is larger than nums2, swap them to ensure n1 is smaller than n2.
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        l = 0
        r = n1
        while l <= r:
            mid1 = (l + r) / 2
            mid2 = (n1 + n2 + 1) / 2 - mid1

            maxLeft1 = nums1[mid1-1] if mid1 != 0 else float('-inf')
            minRight1 = nums1[mid1] if mid1 != n1 else float('inf')

            maxLeft2 = nums2[mid2-1] if mid2 != 0 else float('-inf')
            minRight2 = nums2[mid2] if mid2 != n2 else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (n1 + n2) % 2 == 0:
                    return float(max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return float(max(maxLeft1, maxLeft2))
            elif maxLeft1 > minRight2:
                r = mid1 - 1
            else:
                l = mid1 + 1

        return -1

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = sorted(nums1 + nums2)
        if len(num) % 2 != 0:
            return float(num[(len(num)//2)])
        else:
            return (num[(len(num) // 2) - 1] + num[len(num) // 2]) / 2.0
        

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1+nums2)
        nums.sort()
        if len(nums)%2>0:
            center = int(len(nums)/2)
            return nums[center]     
        center_1, center_2 = int(len(nums)/2)-1, int(len(nums)/2)
        sum_center = nums[center_1]+nums[center_2]
        res = float(sum_center)/float(2)
        return res    

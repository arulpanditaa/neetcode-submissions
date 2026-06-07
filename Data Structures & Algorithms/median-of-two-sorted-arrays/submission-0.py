class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2 , nums1    
        total_left = (len(nums1) + len(nums2) + 1) // 2 
        left = 0 
        right = len(nums1) 

        while left <= right:
            mid = left + (right - left) // 2
            bln = total_left - mid 
            n1_l = nums1[mid-1] if mid > 0 else float('-inf')
            n2_l = nums2[bln-1] if bln > 0 else float ('-inf')
            n1_r = nums1[mid] if mid < len(nums1) else float('inf')
            n2_r = nums2[bln] if bln < len(nums2) else float('inf')

            if n1_r >= n2_l and n1_l <= n2_r:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(n1_l, n2_l)
                else:
                    return (max(n1_l, n2_l) + min(n1_r, n2_r)) / 2 
            elif n1_r < n1_l:
                right = mid - 1
            else:
                left = mid + 1





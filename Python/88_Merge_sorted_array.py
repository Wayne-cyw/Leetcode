class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        p1 = 0
        p2 = 0
        if n == 0:
            return
        for i in range(m + n):
            if p1 == m:
                nums1[i] = nums2[p2]
                p2 += 1
            elif p2 == n:
                nums1[i] = nums3[p1]
                p1 += 1
            elif nums3[p1] <= nums2[p2]:
                nums1[i] = nums3[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
            
    
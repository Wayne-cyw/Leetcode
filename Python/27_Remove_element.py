class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            if nums[p2] == val:
                nums[p2] = '_'
                k += 1
                p2 -= 1
            elif nums[p1] == val:
                nums[p1] = nums[p2]
                nums[p2] = '_'
                p1 += 1
                p2 -= 1
                k += 1
            else:
                p1 += 1
        if p1 == p2 and nums[p1] == val:
            k += 1
            nums[p1] = '_'
        return len(nums) - k
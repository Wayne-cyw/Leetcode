class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.inverse(nums, 0, len(nums))
        self.inverse(nums, k, len(nums))
        self.inverse(nums, 0, k)


        
    def inverse(self, nums: List[int], start: int, end: int) -> None:
        temp = None
        p1 = start
        p2 = end - 1
        while p1 < p2:
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
            p1, p2 = p1 + 1, p2 -1
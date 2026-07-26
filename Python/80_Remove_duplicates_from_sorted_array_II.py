class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        count = 1
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                if count != 1:
                    nums[k + 1] = nums[i - 1]
                k += min(count, 2)
                nums[k] = nums[i]
                count = 1
            else:
                count += 1
        if count >= 2:
            nums[k + 1] = nums[-1]
            return k + 2
        return k + 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError as e:
            for i in nums:
                if i > target:
                    return nums.index(i)
            return len(nums)
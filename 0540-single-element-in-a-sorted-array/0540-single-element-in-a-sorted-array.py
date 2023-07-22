class Solution(object):
    def singleNonDuplicate(self, nums):
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        # If the loop doesn't find the non-duplicate, it means the last element is the single one
        return nums[-1]
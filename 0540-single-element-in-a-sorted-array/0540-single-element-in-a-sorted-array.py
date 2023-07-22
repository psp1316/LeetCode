class Solution(object):
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

        # Ensure mid is at the start of a pair
            if mid % 2 != 0:
                mid -= 1

        # If nums[mid] and nums[mid+1] are different, the single element is to the left
            if nums[mid] != nums[mid + 1]:
                right = mid
        # If nums[mid] and nums[mid+1] are the same, the single element is to the right
            else:
                left = mid + 2

        return nums[left]
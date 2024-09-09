class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return nums[0]
        else: return (sorted(list(set(nums)))[(len(set(nums)))-3] )
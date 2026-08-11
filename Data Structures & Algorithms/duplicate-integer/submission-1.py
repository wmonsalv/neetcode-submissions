class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        transformed = list(set(nums))
        if len(nums) != len(transformed):
            return True
        else:
            return False
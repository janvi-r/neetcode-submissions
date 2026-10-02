class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = set()
        for i in range(len(nums)):
            if nums[i] not in dupl:
                dupl.add(nums[i])
            else:
                return True

        return False
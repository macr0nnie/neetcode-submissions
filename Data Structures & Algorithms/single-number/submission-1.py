class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = 0
        for x in nums:
            seen ^= x
        return seen
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            result.append(nums[i])
        for i in range(0, len(nums)):
            result.append(nums[i])
        return result
        
        
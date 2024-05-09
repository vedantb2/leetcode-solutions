class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)-1):
                if i != j and (nums[i]-1)*(nums[j]-1) > max:
                    max = (nums[i]-1)*(nums[j]-1) 
        return max
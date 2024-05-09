class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyNums = []
        for i in range(0, len(arr)):
            if arr[i] == arr.count(arr[i]):
                luckyNums.append(arr[i])
        if len(luckyNums) > 0:
            return max(luckyNums)
        else: return -1
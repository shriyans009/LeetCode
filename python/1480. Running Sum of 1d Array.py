class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr1 = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            arr1.append(sum)
        return(arr1)

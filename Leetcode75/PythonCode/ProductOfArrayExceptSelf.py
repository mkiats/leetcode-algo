class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultArr = list()

        CurNum = 1
        resultArr.append(1)

        for i in range(len(nums)-1):
            CurNum *= nums[i]
            resultArr.append(CurNum)
        CurNum=1
        for j in reversed(range(1, len(nums))):
            CurNum *= nums[j]
            resultArr[j-1] *= CurNum

        return resultArr

if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([1,2,3,4]))
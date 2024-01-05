import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        smallPtr = sys.maxsize
        midPtr = sys.maxsize

        for i in nums:
            if i <= smallPtr:
                smallPtr = i
            elif i <= midPtr:
                midPtr = i
            else:
                return True
    
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([1,2,3,4,5]))
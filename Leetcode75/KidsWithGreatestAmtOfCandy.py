class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output = []
        threshold = max(candies) - extraCandies
        for j in candies:
            output.append(j>=threshold)
        
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.kidsWithCandies([1,2,3,4], 2))
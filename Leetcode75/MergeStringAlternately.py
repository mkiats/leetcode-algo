class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=""
        letterCountDiff = (len(word1) - len(word2))
        rangeCount = min(len(word1), len(word2))

        for i in range(rangeCount):
            output += word1[i]
            output += word2[i]
        
        if letterCountDiff>0:
            output += word1[rangeCount:]
        elif letterCountDiff<0:
            output += word2[rangeCount:]
        
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternately("abc", "wxyz"))

class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.split(" ")
        output = output[::-1]
        for i in reversed(range(len(output))):
            if output[i] == "":
                output.pop(i)
        return " ".join(output)
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
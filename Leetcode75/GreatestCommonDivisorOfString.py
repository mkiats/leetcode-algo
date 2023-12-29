class Solution:
    def gcd(self, int1, int2):
        if int1==int2:
            return int1
        elif int1>int2:
            return self.gcd(int1-int2, int2)
        else:
            return self.gcd(int1, int2-int1)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2 != str2+str1): 
            return ""
        
        lengthOfGCD = self.gcd(len(str1), len(str2))
        return str1[:lengthOfGCD]
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.gcdOfStrings("ABCABCABC", "ABCABC"))
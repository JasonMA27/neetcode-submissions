class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        BI = str(x)

        return BI == BI[::-1]


        
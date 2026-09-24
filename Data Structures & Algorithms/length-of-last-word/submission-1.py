class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        s = s.strip()
        lastWord = ""

        for c in s[::-1]:
            lastWord += c
            if c == " ":
                return len(lastWord) - 1
    
        return len(lastWord)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = "abc"
        word2 = "pqr"

        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        word1 = word1.replace('c', '')
        word2 += 's'
        result1 = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result1 += word1[i]
            if i < len(word2):
                result1 += word2[i]
        return result
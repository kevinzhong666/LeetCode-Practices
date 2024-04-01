class Solution(object):
    def mergeAlternately(self, word1, word2):
        output = ''
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                output += word1[i]
                i += 1
            if j < len(word2):
                output += word2[j]
                j += 1
        return output


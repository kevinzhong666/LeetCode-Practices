class Solution:
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        s = list(s)  # Convert to list to modify
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]  # Swap vowels
                i += 1
                j -= 1
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1

        return ''.join(s)  # Convert list back to string

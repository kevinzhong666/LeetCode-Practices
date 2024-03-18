class Solution(object):
    def reverseWords(self, s):
        # Strip leading and trailing spaces, and then split the string into words
        split_txt = s.strip().split()

        # Reverse the list of words
        reversed_txt = split_txt[::-1]

        # Join the reversed list back into a string with a space between words
        return ' '.join(reversed_txt)

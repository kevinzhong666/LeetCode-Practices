class Solution(object):
    def largestAltitude(self, gain):
        current_alt = 0
        highest_alt = 0

        for g in gain:
            current_alt += g
            highest_alt = max(highest_alt, current_alt)
        return highest_alt

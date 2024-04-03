class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0  # Initialize count of flowers that can be planted
        i = 0
        length = len(flowerbed)

        while i < length:
            # Check if the current spot is empty, and ensure neighbors (if they exist) are also empty.
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Plant a flower here
                count += 1  # Increment the count
                i += 1  # Skip the next spot since a flower was just planted
            if count >= n:
                return True  # Early exit if we've planted enough flowers
            i += 1

        return count >= n  # Check if we've been able to plant at least 'n' flowers


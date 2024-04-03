class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        while i < length and n > 0:
            # Check if current spot is empty.
            if flowerbed[i] == 0:
                # Check for first position, last position, and general case with two neighbors.
                is_first_or_no_left_neighbor = (i == 0 or flowerbed[i - 1] == 0)
                is_last_or_no_right_neighbor = (i == length - 1 or flowerbed[i + 1] == 0)

                if is_first_or_no_left_neighbor and is_last_or_no_right_neighbor:
                    # Plant a flower here.
                    flowerbed[i] = 1
                    # Decrement n because we have successfully planted one flower.
                    n -= 1
                    # Skip the next spot to ensure no adjacent planting.
                    i += 1

            # Move to the next spot.
            i += 1

        # If n has been reduced to 0, it means we could plant all flowers without breaking the rule.
        return n == 0


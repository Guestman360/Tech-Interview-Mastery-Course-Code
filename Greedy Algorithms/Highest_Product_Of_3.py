def maximumProduct(nums):
    min1, min2 = 0, 0
    max1, max2, max3 = 0, 0, 0

    for number in nums:
        if number <= min1:
            min2 = min1
            min1 = number
        elif number <= min2:
            min2 = number
        if number >= max1:
            max3 = max2
            max2 = max1
            max1 = number
        elif number >= max2:
            max3 = max2
            max2 = number
        elif number >= max3:
            max3 = number
    return max(min1 * min2 * max1, max1 * max2 * max3)
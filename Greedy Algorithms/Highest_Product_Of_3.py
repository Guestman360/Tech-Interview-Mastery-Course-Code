# Brute Force
def maxProduct(arr, n): 
  
    # if size is less than 3, 
    # no triplet exists 
    if n < 3: 
        return -1
  
    # will contain max product 
    max_product = -(sys.maxsize - 1) 
      
    for i in range(0, n - 2): 
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n): 
                max_product = max( 
                    max_product, arr[i] 
                    * arr[j] * arr[k]) 
  
    return max_product

# Slight Improvement - (n log n) solution
def maxProductOfThree(nums):
    sortedNums = nums.sort()
    length = len(sortedNums)

    return sortedNums[length - 1] * sortedNums[length - 2] * sortedNums[length - 3]

# Final Solution
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
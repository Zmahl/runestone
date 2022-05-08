

def binary_search(nums, target):

    if len(nums) == 0:
        return False

    else:
        middle = len(nums) // 2

        if nums[middle] == target:
            return True
    
        elif nums[middle] < target:

            return binary_search(nums[middle + 1:], target)
    
        else:

            return binary_search(nums[:middle], target)

    

print(binary_search([3, 5, 6, 8, 11, 12, 14, 15, 17, 18], 17))
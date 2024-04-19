
# the Kadane algorithm which has a time complexity of O(n), where n is the length of the input array.
def max_subarray_sum(nums):
    if not nums:
        return 0
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Take input for the array from the user
nums = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]

print("Maximum sum of subarray:", max_subarray_sum(nums))


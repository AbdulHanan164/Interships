#TASK 1 Rotate Array Algorithm
def rotate_array(arr, steps):
    if not arr:
        return arr
    n = len(arr)
    steps %= n
    if steps == 0:
        return arr
    if steps < 0:
        steps += n
    reverse(arr, 0, n - 1)
    # Reverse the first 'steps' elements
    reverse(arr, 0, steps - 1)
    reverse(arr, steps, n - 1)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
# Take input from the user
arr_str = input("Enter the elements of the array separated by spaces: ")
arr = [int(x) for x in arr_str.split()]
steps = int(input("Enter the number of steps to rotate the array: "))
# Rotate the array
rotate_array(arr, steps)
print("Rotated array:", arr)




def binary_search(arr, target):
  if (not arr or len(arr) == 0): return -1
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      right = mid - 1
    else:
      left = mid + 1
  
nums = [2, 5, 6, 12, 12, 12, 23, 45, 78, 90]

index = binary_search(nums, )

if (index and index >= 0):
  print('found at {}'.format(index))
else:
  print('not found at anywhere')
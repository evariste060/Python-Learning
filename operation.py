nums = [1, 2, 2, 1, 1, 0]

write = 0
read = 1

while read < len(nums):
    if nums[write] == nums[read] and nums[write] != 0:
        nums[write] *= 2
        nums[read] = 0
        write += 1
        read += 1
    elif nums[write] == 0:
        write += 1
    else:
        write += 1
        read += 1

print(nums)
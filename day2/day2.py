
def in_range(num):
    numabs = abs(num)
    return numabs > 0 and numabs <= 3

input = open("day2/input.txt", "r")

lines = input.readlines()

def is_safe(nums):
    is_increasing = True
    prev_num = nums[0]
    if (prev_num > nums[1]):
        is_increasing = False
    for num in nums[1:]:
        if (is_increasing):
            if (num < prev_num or not in_range(prev_num - num)):
                return False
        else:
            if (num > prev_num or not in_range(num - prev_num)):
                return False
        prev_num = num
    return True

level_safe = [True] * len(lines)
for i, line in enumerate(lines):
    nums = [int(x) for x in line.split()]
    s = is_safe(nums)
    # round 2 try and remove each number and see if it is safe
    if (s is False):
        print("false")
        safe = False
        for j in range(0, len(nums)):
            nums2 = nums[:j] + nums[j + 1:]
            if (is_safe(nums2)):
                safe = True
                break
        level_safe[i] = safe
    # if (not level_safe[i]):
    #     print("Unsafe line", i, nums)
        

print(level_safe)

safe_count = 0
for s in level_safe:
    safe_count += 1 if s else 0
    
print(safe_count)
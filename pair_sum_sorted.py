import sys


def pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        result = nums[left] + nums[right]
        if result < target:
            left += 1
        elif result > target:
            right -= 1
        else:
            return [left, right]

    return []


nums = [1, 3, 4, 9, 12, 18]
target = 15

arguments = sys.argv
if len(arguments) > 1:
    str_nums = arguments[1].split(" ")
    nums = [int(x) for x in str_nums]
    target = int(arguments[2])

    print(
        f"pair_sum_sorted({', '.join([str(x) for x in nums])}, {target}) = {pair_sum_sorted(nums, target)}"
    )
else:
    print("python3 pair_sum_sorted.py '1 2 3' 4")

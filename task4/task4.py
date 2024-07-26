with open(input(), "r") as f:
    nums = [int(num) for num in f.read().split()]


def min_steps(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    steps = 0
    for num in nums:
        steps += abs(num - median)
    return steps


print(min_steps(nums))

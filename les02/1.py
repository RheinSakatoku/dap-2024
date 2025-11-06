print("Введи числа через пробел")
nums = list(map(int, input().split()))

print("Введи таргет")
target = int(input())

def checker(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

print(checker(nums, target))
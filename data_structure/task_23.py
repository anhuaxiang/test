def solu(nums, target):
    if target not in nums:
        return [-1, -1]
    equal = []
    for i in range(len(nums)):
        if nums[i] == target:
            equal.append(i)
    return [min(equal), max(equal)]


if __name__ == '__main__':
    print(solu(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solu([1, 1, 1], 1))
    print(solu(nums=[5, 7, 7, 8, 8, 10], target=6))

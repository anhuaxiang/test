def remove(nums):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] > nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return len(set(nums))


def remove_2(nums, val):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return i


def str_str(haystack, needle):
    length = len(needle)
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + length] == needle:
            return i
    return -1


def divide(dividend, divisor):
    flag = not (dividend > 0) ^ (divisor > 0)
    count = 0
    while abs(dividend) >= abs(divisor):
        if flag:
            count += 1
            dividend -= divisor
        else:
            count -= 1
            dividend += divisor
    if pow(-2, 31) >= count or count > pow(2, 31):
        return pow(2, 31) - 1
    return count


def divide_1(dividend, divisor):
    flag = -1 if (dividend > 0) ^ (divisor > 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    if dividend < divisor:
        return 0
    if dividend == divisor:
        return flag
    if divisor == 1:  # 防止2**31
        return flag * dividend if flag * dividend < 2 ** 31 else 2 ** 31 - 1
    return flag * len(range(divisor, dividend + 1, divisor))


def pow_x_n(x, n):
    return pow(x, n)


def search_insert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        index = 0
        for i in nums:
            if i <= target:
                index += 1
            else:
                nums.insert(index, target)
                break
        return index

if __name__ == '__main__':
    # a = [0, 1, 2, 2, 3, 0, 4, 2]
    # print(remove_2(a, 2))
    # print(a)
    # print(str_str('hello', ''))
    # print(divide(-2147483648, 2))
    # print(divide_1(-2147483648, -2))
    # print(pow_x_n(2.00000, 10))
    print(search_insert([1, 3, 5, 6], 5))
    print(search_insert([1, 3, 5, 6], 2))
    print(search_insert([1, 3, 5, 6], 7))
    print(search_insert([1, 3, 5, 6], 0))
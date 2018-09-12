
def findMedianSortedArrays(nums1, nums2):
    nums1 = nums1 + nums2
    nums1.sort()
    if len(nums1) % 2 == 1:
        return nums1[len(nums1)//2]
    else:
        return (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]

    a = findMedianSortedArrays(nums1, nums2)
    print(a)
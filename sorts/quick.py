# coding:utf-8
# author:zlikun

# 待排序列表
lst = [27, 12, 16, 32, 71, 69, 21, 12, 44]

# ---------------------------------- 本段逻辑仅供调试、理解之用 ---------------------------------------

# 以第一个元素作为支点
pivot = lst[0]
# 遍历列表，使后续元素与支点比较，小的放左边，大的放右边
# 为了不额外消耗存储空间，移动过程中，使用支点的空位来存放移动的元素
# 当左边留出空位后，应从右边开始继续比较，以便于将得以元素写入左边的空位，反之亦然，
# 直到标记左右空位的标志相等时，一轮比较结束
low = 0
high = len(lst) - 1
# 定义一个方向变量，True表示从左向右，False表示从右向左
dr = False
while low < high:

    if dr:
        # 从左向各，如果比支点大，应交换到右边，并修改遍历方向变量，使从右向左遍历
        if pivot < lst[low]:
            lst[high] = lst[low]
            high -= 1
            dr = False
        else:
            low += 1
    else:
        # 从右向左，如果比支点小，应交换到左边，并修改遍历方向变量，使从左向右遍历
        if pivot > lst[high]:
            # low的位置为支点，所以可以直接赋值
            lst[low] = lst[high]
            # low向右移，此时high指向被交换的值，由于已赋值给左边空位，所以成为右边的空位
            low += 1
            dr = True
        else:
            high -= 1

# 此时low == high，所以取任意值即可
lst[low] = pivot

print(lst)


# ---------------------------------- 快速排序实现 ---------------------------------------

def quick_sort(lst, left, right):
    '''
    快速排序，这里使用了遍历方向变量，也可以不使用方向变量
    :param lst:
    :param left:
    :param right:
    :return:
    '''
    # 当left与right相等时，排序即完成
    if left >= right:
        return

    # 以第一个元素作为支点
    pivot = lst[left]
    # 遍历列表，使后续元素与支点比较，小的放左边，大的放右边
    # 为了不额外消耗存储空间，移动过程中，使用支点的空位来存放移动的元素
    # 当左边留出空位后，应从右边开始继续比较，以便于将得以元素写入左边的空位，反之亦然，
    # 直到标记左右空位的标志相等时，一轮比较结束
    low = left
    high = right
    # 定义一个方向变量，True表示从左向右，False表示从右向左
    dr = False
    while low < high:

        if dr:
            # 从左向右，如果比支点大，应交换到右边，并修改遍历方向变量，使从右向左遍历
            if pivot < lst[low]:
                lst[high] = lst[low]
                high -= 1
                dr = False
            else:
                low += 1
        else:
            # 从右向左，如果比支点小，应交换到左边，并修改遍历方向变量，使从左向右遍历
            if pivot > lst[high]:
                # low的位置为支点，所以可以直接赋值
                lst[low] = lst[high]
                # low向右移，此时high指向被交换的值，由于已赋值给左边空位，所以成为右边的空位
                low += 1
                dr = True
            else:
                high -= 1

    # 此时low == high，所以取任意值即可
    lst[low] = pivot

    # 第一轮完成后，递归排序左右两部分数据
    # 注意递归时，不包含支点数据，支点已是正确位置，无需再参与后续排序
    quick_sort(lst, left, low - 1)
    quick_sort(lst, low + 1, right)


# 待排序列表
lst = [27, 12, 16, 32, 71, 69, 21, 12, 44]

quick_sort(lst, 0, len(lst) - 1)
# [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(lst)


# ---------------------------------- 快速排序实现 ---------------------------------------


def quick_sort2(lst, left, right):
    '''
    快速排序，不使用方向变量
    :param lst:
    :param left:
    :param right:
    :return:
    '''
    if left >= right:
        return

    pivot = lst[left]
    low = left
    high = right
    while low < high:

        # 先从右向左，是因为第一个空位在左边(支点位置)

        # 从右向左比较，直到找到元素值比支点大的(需要放在支点左边)
        while low < high and pivot <= lst[high]:
            high -= 1

        # 此时 high　指向元素应放在支点左边空位上，然后 high 即为空位
        lst[low] = lst[high]

        # 从左向右比较，直到找到元素值比支点小的(需要放在支点右边)
        while low < high and pivot >= lst[low]:
            low += 1

        # 此时 low　指向元素应放在支点右边空位上，然后 low 即为空位
        lst[high] = lst[low]

    # 此时 low == high，为支点值，支点此时正好放在正确的位置上了(无论升序还是降序，其所在位置都是正确的)
    lst[low] = pivot

    quick_sort2(lst, left, low - 1)
    quick_sort2(lst, low + 1, right)


# 待排序列表
lst = [27, 12, 16, 32, 71, 69, 21, 12, 44]

quick_sort2(lst, 0, len(lst) - 1)
# [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(lst)

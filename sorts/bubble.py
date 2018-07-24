# coding:utf-8
# author:zlikun

# 待排序列表
lst = [27, 12, 36, 12, 24, 45, 68, 59, 91]

# [12, 27, 16, 32, 71, 69, 21, 12, 44]
print(lst)

# http://python.jobbole.com/82270/
# https://www.cnblogs.com/qlshine/p/6017957.html
# https://www.cnblogs.com/shen-hua/p/5422676.html

# 取列表中的元素，与列表中的其它元素依次比较，大则交换
# 时间复杂度是O(N^2)，是一种稳定排序算法，但效率比较低

# 外层循环用于控制排序循环趟数( n - 1 )
for i in range(len(lst) - 1):
    # 每趟循环结束后，将序列内的最大值交换到序列的最后位置上，
    # 下一趟循环结束位置-1，直到收缩到只有一个元素时(最小元素)
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(lst)

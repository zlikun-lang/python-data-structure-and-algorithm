# 待排序列表
lst = [12, 27, 16, 32, 71, 69, 21, 12, 44]

# [12, 27, 16, 32, 71, 69, 21, 12, 44]
print(lst)


# 希尔排序，是插入排序的一种，是一种更高效的改进版本，参考：
# http://python.jobbole.com/82270/
# https://www.cnblogs.com/0zcl/p/6680652.html
# https://www.cnblogs.com/xubing-613/p/7286203.html
# https://www.cnblogs.com/chengxiao/p/6104371.html
# http://www.iqiyi.com/v_19rrhzyejc.html

# 参考书籍：
# 《数据结构与问题求解（第四版）》 第8.4节
# 《Java数据结构和算法（第二版）》 第7章
# 《Algorithms 4th》 第2.1.6节

# 一个插入排序函数，步长由外部指定(简单插入排序步长为1)
# 步长(增量)表示分组数量
def shell_sort_once(lst, gap):
    for i in range(gap, len(lst)):
        key = lst[i]
        j = i - gap
        while j >= 0:
            if lst[j] > key:
                lst[j + gap], lst[j] = lst[j], key
            else:
                break
            j -= gap


# 分步骤说明希尔排序过程

# 4  ->  [12, 27, 16, 12, 44, 69, 21, 32, 71]
gap = len(lst) // 2
shell_sort_once(lst, gap)
print(gap, ' -> ', lst)

gap = gap // 2
shell_sort_once(lst, gap)
# 2  ->  [12, 12, 16, 27, 21, 32, 44, 69, 71]
print(gap, ' -> ', lst)

gap = gap // 2
shell_sort_once(lst, gap)
# 1  ->  [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(gap, ' -> ', lst)

# 将算法整合
lst = [12, 27, 16, 32, 71, 69, 21, 12, 44]
# [12, 27, 16, 32, 71, 69, 21, 12, 44]
print(lst)

gap = len(lst) // 2
while gap > 0:
    shell_sort_once(lst, gap)
    gap //= 2

# [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(lst)

# 直接将步长设置为1，即可完成排序，但这种方式是将排序退化为简单插入排序，性能较差
# 通过若干次分组排序后，最后一次完成整体排序，性能较好
lst = [12, 27, 16, 32, 71, 69, 21, 12, 44]

shell_sort_once(lst, 1)

# [12, 12, 16, 21, 27, 32, 44, 69, 71]
print(lst)

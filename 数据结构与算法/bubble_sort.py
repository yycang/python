########
# 冒泡排序
########

"""
算法运作:
1.比较相邻两个值的大小, 如果前者比后者大(升序排列), 则交换它们的值
2.对每个相邻的元素进行如上比较, 一直比较到最后, 则最后那个为最大的数
3.重复上述操作, 除了最大的那个
4.持续对越来越少的数进行上述操作, 直到没有一个数可以比较

"""


def bubble_sort(li):
    n = len(li)
    for i in range(n-1, 0, -1):
        # i表示要遍历的次数, 逐次减少
        for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

li = [1, 4, 5, 7, 8, 23, 41, 1]
bubble_sort(li)
print(li)

"""

时间复杂度:
        最优时间复杂度:   O(n), 即遍历一次完成排序
        最坏时间复杂度:   O(n^2)
        稳定性:    稳定

"""
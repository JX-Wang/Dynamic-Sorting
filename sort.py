#! /usr/bin/env python
# coding:utf-8
'''
排序分析
========
author@wud
date:2018/7/2
--------------
date:2018/7/4
History: 原本是要放在后台进行排序，排序之后将结果进行分析的CS框架
但是开题的时候因为一些问题导致分数特别低(早上开题迟到)，只能修改构架
放弃CS框架，开始学习Tkinter，实现排序过程可视化。
Requests--
    算法方面：-比较类排序和非比较类排序(桶排序)-
    GUI方面：-可视化排序过程，多种兼容-
   *增加方面：-数据的查找-
   *数据要求：-大数据-
Points--
    1.数据的移动和处理，线条的覆盖问题
    2.对于不同排序的特殊数据的显示
'''

from Tkinter import *
import random
import time
import os
import math
from PIL import Image
from PIL import ImageTk


sort = Tk()
sort.title("数的排序")
sort.geometry('280x150')  # 宽 X 长
sort.resizable(width=True, height=True)


def quicksort(random_set, start, end, divide_set, quick_sort_):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = random_set[i]
        # 显示画布
        divide_set[i] = Canvas(quick_sort_, width=1, height=1100, background="#585b65")
        divide_set[i].place(x=3 * i + 1, y=random_set[i], anchor=NW)
        quick_sort_.update()  # 显示

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (random_set[j] <= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等

            # 此时random_set[i]的值要比random_set[j]要大，所以random_set[i]画布的长度很长，将random_set[i]画布归为背景
            divide_set[i] = Canvas(quick_sort_, width=1, height=1200, background="white")
            divide_set[i].place(x=3 * i + 1, y=1200, anchor=NW)
            quick_sort_.update()  # 更新

            random_set[i] = random_set[j]
            divide_set[i] = Canvas(quick_sort_, width=1, height=1200, background="#82b6d2")
            divide_set[i].place(x=3 * i + 1, y=random_set[j], anchor=NW)
            quick_sort_.update()  # 更新

            # 同样的方式比较前半区
            while (i < j) and (random_set[i] >= base):
                i = i + 1
            divide_set[i] = Canvas(quick_sort_, width=1, height=1200, background="white")
            divide_set[i].place(x=3 * i + 1, y=1200, anchor=NW)
            quick_sort_.update()  # 更新

            random_set[j] = random_set[i]
            divide_set[j] = Canvas(quick_sort_, width=1, height=1200, background="#82b6d2")
            divide_set[j].place(x=3 * j + 1, y=random_set[i], anchor=NW)
            quick_sort_.update()  # 更新

            # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        random_set[i] = base
        divide_set[i] = Canvas(quick_sort_, width=1, height=1200, background="#de0b0b")  # 所选基数展示(红色)
        divide_set[i].place(x=3 * i + 1, y=base, anchor=NW)
        quick_sort_.update()  # 显示

        divide_set[i] = Canvas(quick_sort_, width=1, height=1200, background="#82b6d2")  # 所选基数展示(恢复)
        divide_set[i].place(x=3 * i + 1, y=base, anchor=NW)

        # 递归前半区
        quicksort(random_set, start, i - 1, divide_set, quick_sort_)
        # 递归后半区
        quicksort(random_set, j + 1, end, divide_set, quick_sort_)


def MinSort(arr, start, end, heap_sort_func, divide_set):
    '''
    :param arr:
    :param start:
    :param end:
    :param heap_sort_func:
    :param divide_set:
    :return:
    '''
    arrHeight = 0
    for index in range(0, end - start):
        if index == 2 ** (arrHeight + 1) - 1:
            arrHeight = arrHeight + 1  # 堆的高度
    color_list = ["red", "green", "black", "blue", "pink", "yellow", "grey", "orange"]
    for NodeIndex in range(2 ** (arrHeight) - 2, -1, -1):
        color = color_list[random.randint(0, 7)]
        currentNode = arr[NodeIndex + start]  # 目前的节点的值等于数组[index节点-开始]
        childIndex = NodeIndex * 2 + 1 + start  # 儿子节点等于index节点*2+1+start

        if childIndex + 1 > len(arr):
            continue
        else:
            leftChild = arr[childIndex]  # 左孩子为数组的左孩子节点
            # color = color_list[random.randint(0, 7)]
            if currentNode > leftChild:  # 如果现在的节点大于左孩子节点
                # 定义画布显示当前节点
                divide_set[NodeIndex + start] = Canvas(heap_sort_func, width=1, height=1100, background="red")
                divide_set[NodeIndex + start].place(x=3 * (NodeIndex + start) + 1, y=currentNode)
                heap_sort_func.update()

                # 定义画布显示儿子节点
                divide_set[childIndex] = Canvas(heap_sort_func, width=1, height=1100, background="#f0efef")
                divide_set[childIndex].place(x=3 * childIndex + 1, y=leftChild)
                heap_sort_func.update()
                # 以上程序没有问题

                # 交换Y
                currentNode, leftChild = leftChild, currentNode

                # 交换节点
                arr[childIndex] = leftChild
                arr[NodeIndex + start] = currentNode

                # 交换画布
                divide_set[NodeIndex + start], divide_set[childIndex] = divide_set[childIndex], divide_set[
                    NodeIndex + start]
                heap_sort_func.update()

                # 恢复，并准备下一次展示
                divide_set[childIndex] = Canvas(heap_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[childIndex].place(x=3 * childIndex + 1, y=leftChild)
                divide_set[NodeIndex + start] = Canvas(heap_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[NodeIndex + start].place(x=3 * (NodeIndex + start) + 1, y=currentNode)
                heap_sort_func.update()


        if childIndex + 1 >= len(arr):
            continue
        else:
            rightChild = arr[childIndex + 1]

            if currentNode > rightChild:
                divide_set[NodeIndex + start] = Canvas(heap_sort_func, width=1, height=1100, background="red")
                divide_set[NodeIndex + start].place(x=3 * (NodeIndex + start) + 1, y=currentNode)
                heap_sort_func.update()
                divide_set[childIndex] = Canvas(heap_sort_func, width=1, height=1100, background="#f0efef")
                divide_set[childIndex].place(x=3 * childIndex + 1, y=rightChild)
                heap_sort_func.update()
                # 以上程序也没有问题

                # 交换Y
                currentNode, rightChild = rightChild, currentNode

                # 交换节点
                arr[childIndex] = rightChild
                arr[NodeIndex + start] = currentNode

                # 交换画布
                divide_set[NodeIndex + start], divide_set[childIndex] = divide_set[childIndex], divide_set[
                    NodeIndex + start]
                heap_sort_func.update()

                # 恢复，并准备下一次展示
                divide_set[childIndex] = Canvas(heap_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[childIndex].place(x=3 * childIndex + 1, y=rightChild)
                divide_set[NodeIndex + start] = Canvas(heap_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[NodeIndex + start].place(x=3 * (NodeIndex + start) + 1, y=currentNode)
                heap_sort_func.update()


def HeapSort(arr, heap_sort_func, divide_set):
    '''
    :param arr:
    :param heap_sort_func:
    :param divide_set:
    :return: 经过对排序的有序序列
    '''
    for i in range(0, len(arr) - 1):
        MinSort(arr, i, len(arr), heap_sort_func, divide_set)
    return arr


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def ConfiationAlgorithm(random_set, guibing_sort_Canv, divide_set):
    '''
    :param random_set:
    :param guibing_sort_Canv:
    :param divide_set:
    :return: 归并排序后的有序结果集合
    '''
    flag = 0
    num_left = 0
    num_right = 0
    if len(random_set) <= 1:  # 子序列
        return random_set
    mid = (len(random_set) / 2)  # 取中间值
    divide_set[mid] = Canvas(guibing_sort_Canv, width=1, height=1100, background="red")
    divide_set[mid].place(x=3*mid+1, y=random_set[mid])
    guibing_sort_Canv.update()
    '''
    divide_set[mid] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#82b6d2")
    divide_set[mid].place(x=3*mid+1, y=random_set[mid])
    guibing_sort_Canv.update()
    '''
    left = ConfiationAlgorithm(random_set[:mid], guibing_sort_Canv, divide_set)  # 递归的切片操作
    right = ConfiationAlgorithm(random_set[mid:len(random_set)], guibing_sort_Canv, divide_set)
    result = []
    # i,j = 0,0

    while len(left) > 0 and len(right) > 0:
        if (left[0] >= right[0]):
            # print left, type(left), len(left)
            # print left[0], right[0]
            # result.append(left[0])
            position = num_left + flag
            temp = left[0]
            result.append(left.pop(0))
            divide_set[num_left] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#82b6d2")
            divide_set[num_left].place(x=3 * position + 1, y=temp)
            divide_set[position] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#1bf956")
            divide_set[position].place(x=3 * position + 1, y=right[0])
            # guibing_sort_Canv.update()
            divide_set[num_left], divide_set[position] = divide_set[position], divide_set[num_left]
            # guibing_sort_Canv.update()
            num_left += 1
            # i += 1
        else:
            # result.append(right[0])
            position = num_left + flag
            temp = right[0]
            result.append(right.pop(0))
            divide_set[num_left] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#82b6d2")
            divide_set[num_left].place(x=3 * position + 1, y=temp)
            divide_set[position] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#1bf956")
            divide_set[position].place(x=3 * position + 1, y=left[0])
            # guibing_sort_Canv.update()
            divide_set[num_left], divide_set[position] = divide_set[position], divide_set[num_left]
            num_left += 1
            # guibing_sort_Canv.update()
        # 更新位置的选择
        guibing_sort_Canv.update()
    flag = 2 * num_left
    print flag, num_left
    # 并过程
    if (len(left) > 0):
        result.extend(ConfiationAlgorithm(left, guibing_sort_Canv, divide_set))
    else:
        result.extend(ConfiationAlgorithm(right, guibing_sort_Canv, divide_set))
    # 返回有序数列
    return result


def quick_sort_func():
    '''
    :parameter 随机无序数组random_set[]和其对应的画布集合，快速排序算法的实现
    :return: 有序的排序数组和对应的画布对象集合
    '''

    # 显示界面的搭建
    quick_sort_ = Tk()
    quick_sort_.title("快速排序结果")
    quick_sort_.geometry('2400x1200')
    quick_sort_.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["red", "green", "black", "blue", "pink", "yellow", "grey", "orange"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合

    # 开始产生随机数，并对每个随机数规定一个画布
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(quick_sort_, width=1, height=1200)  # 给每个画布对象进行定义

    # 展示无序数列
    '''
    for l in range(num + 1):
        divide_set[l] = Canvas(quick_sort_, width=1, height=1100, background="#82b6d2")
        divide_set[l].place(x=3 * l + 1, y=random_set[l])
    '''
    # 计时
    time_start = time.time()  # 开始时间
    quicksort(random_set, 0, num, divide_set, quick_sort_)
    time_end = time.time()  # 结束时间

    # 开始对随机数进行排序
    # 结束
    # 给每个随机数对应的画布上色并进行展示
    # 耗时结果展示
    time_used = "%.5f" % float(time_end - time_start)
    time_lable = Label(quick_sort_, text="排序耗时:" + str(time_used), width=20, height=1)
    time_lable.pack(side=LEFT, anchor=N)
    # quick_sort_func循环打开
    quick_sort_.mainloop()


def sheel_sort_func():
    sheel_sort_func = Tk()
    sheel_sort_func.title("希尔排序")
    sheel_sort_func.geometry('2400x1200')
    sheel_sort_func.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(sheel_sort_func, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义
    # 开始对随机数进行排序

    time_start = time.time()  # 开始时间
    random_set = shell_sort(random_set)
    time_end = time.time()  # 结束时间

    # 开始对随机数进行排序
    # 结束
    # 给每个随机数对应的画布上色并进行展示
    for l in range(num - 1):
        # print random_set[l]
        divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    # 耗时结果展示
    time_used = "%.5f" % float(time_end - time_start)
    time_lable = Label(sheel_sort_func, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # quick_sort_func循环打开
    sheel_sort_func.mainloop()
    return


def maopao_sort_func():
    """
    :parameter 随机无序数组random_set[]和其对应的画布集合，冒泡排序算法进行排序
    :return 有序的数组和对应的画布对象集合
    """
    maopao_sort_func = Tk()
    maopao_sort_func.title("冒泡排序演示")
    maopao_sort_func.geometry('2400x1200')
    maopao_sort_func.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    # print "数量:", num
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合

    # 产生随机数，并对每个随机数定义一个画布
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(maopao_sort_func, width=1, height=1100)  # 给每个画布对象进行定义
    # 开始对随机数进行排序
    # random_set.sort()

    # 冒泡排序开始
    time_start = time.time()
    for j in range(num - 1):
        for k in range(num - 1 - j):
            if random_set[k] < random_set[k+1]:
                """
                title: 排序过程的动态展示
                attention:对比位用与其他位置不同颜色的线展示(考虑点:线条粗细，线条颜色；)
                """
                # 定义画布并显示较大的数
                divide_set[k] = Canvas(maopao_sort_func, width=1, height=1100)
                divide_set[k].place(x=3 * k + 1, y=random_set[k], anchor=NW)
                maopao_sort_func.update()  # 显示

                # 定义画布并显示较小的数
                divide_set[k+1] = Canvas(maopao_sort_func, width=1, height=1100)
                divide_set[k+1].place(x=3 * k + 4, y=random_set[k+1], anchor=NW)
                maopao_sort_func.update()  # 显示

                # 交换顺序
                random_set[k], random_set[k + 1] = random_set[k + 1], random_set[k]
                divide_set[k], divide_set[k+1] = divide_set[k+1], divide_set[k]
                maopao_sort_func.update()  # 清空上面的两个逆序画布，得到有序的画布

                # 恢复颜色，填充有序的数据，并准备进行下一轮演示
                divide_set[k] = Canvas(maopao_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[k].place(x=3*k + 1, y=random_set[k])
                divide_set[k+1] = Canvas(maopao_sort_func, width=1, height=1100, background="#82b6d2")
                divide_set[k+1].place(x=3*k + 4, y=random_set[k+1])
                maopao_sort_func.update()

                # divide_set[k], divide_set[k+1] = divide_set[k+1], divide_set[k]
                # divide_set[k].place(x=3 * k + 1, y=1200 - random_set[k], anchor=NE)
    # 结束
    time_end = time.time()
    # 给每个随机数对应的画布上色并进行展示
    # for l in range(num - 1):
        # print random_set[l]
        # divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    time_used = "%.5f" % float(time_end - time_start)

    # 耗时结果展示
    print time_used
    time_used = "%.5f" % float(time_end - time_start)
    time_lable = Label(maopao_sort_func, text="排序耗时:" + str(time_used), width=20, height=1, fg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # maopao_sort_func循环打开
    maopao_sort_func.mainloop()


def guibing_sort_func():
    guibing_sort_Canv = Tk()
    guibing_sort_Canv.title("归并排序")
    guibing_sort_Canv.geometry('2400x1200')
    guibing_sort_Canv.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(guibing_sort_Canv, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义

    # 展示
    for l in range(len(random_set) - 1):
        divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
        guibing_sort_Canv.update()
    # 开始对随机数进行排序
    # 开始计时
    time_start = time.time()
    ConfiationAlgorithm(random_set, guibing_sort_Canv, divide_set)
    time_end = time.time()

    time_used = "%.5f" % float(time_end - time_start)

    # 打印画布
    # random_set = random_set[::-1]
    # for l in range(num - 1):
    #     divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    #  花费时间
    print time_used
    # 耗时展示
    time_lable = Label(guibing_sort_Canv, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # select_sort_func循环打开
    guibing_sort_Canv.mainloop()
    return


def select_sort_func():
    select_sort_func = Tk()
    select_sort_func.title("快速选择排序")
    select_sort_func.geometry('2400x1200')
    select_sort_func.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(select_sort_func, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义

    # 开始对随机数进行排序
    # 开始计时
    time_start = time.time()
    for j in range(num - 1):
        min_index = j
        for k in range(j + 1, num):
            if random_set[k] < random_set[min_index]:
                min_index = k
            # 交换位置
            if min_index != j:
                random_set[j], random_set[min_index] = random_set[min_index], random_set[j]
    time_end = time.time()

    time_used = "%.5f" % float(time_end - time_start)

    # 打印画布
    for l in range(num - 1):
        divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    #  花费时间
    print time_used
    # 耗时展示
    time_lable = Label(select_sort_func, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # select_sort_func循环打开
    select_sort_func.mainloop()


def insert_sort_func():
    insert_sort_func = Tk()
    insert_sort_func.title("插入排序")
    insert_sort_func.geometry('2400x1200')
    insert_sort_func.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(insert_sort_func, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义
    # 开始对随机数进行排序
    time_start = time.time()
    random_set = insert_sort(random_set)
    time_end = time.time()

    time_used = "%.5f" % float(time_end - time_start)

    # 打印画布
    for l in range(num - 1):
        divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    #  花费时间
    print time_used
    # 耗时展示
    time_lable = Label(insert_sort_func, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # select_sort_func循环打开
    insert_sort_func.mainloop()

    return


def bucket_sort(random_set, bucket_sort_Canv, divide_set):
    '''
    :param random_set:
    :param bucket_sort_Canv:
    :param divide_set:
    :return: 经过基数排序形成的有序序列
    :argument: bucket排序的特殊之处在于不是基于比较类的排序，不易使用画布进行处理
    '''
    # 展示无序数列
    for i in range(len(random_set) - 1):
        divide_set[i] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#82b6d2")  # 定义画布
        divide_set[i].place(x=3*i+1, y=random_set[i])
        bucket_sort_Canv.update()

    # 先根据数据来定义桶的数量
    buckets = [0] * ((max(random_set) - min(random_set))+1)
    # 桶中每个数都+1
    for i in range(len(random_set)):
        # divide_set[i] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#82b6d2")
        buckets[random_set[i]-min(random_set)] += 1
        #print random_set[i] - min(random_set)

        divide_set[random_set[i] - min(random_set)] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#1bf956")
        divide_set[random_set[i]-min(random_set)].place(x=random_set[i]-min(random_set), y=random_set[random_set[i]-min(random_set)])
        bucket_sort_Canv.update()  # 显示

    # 定义一个集合用来存放序列
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(random_set)]*buckets[i]
            divide_set[i] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#f0efef")
            divide_set[i].place(x=3 * i + 1, y=1100)
            bucket_sort_Canv.update()
            # f0efef
            divide_set[i] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#1bf956")
            divide_set[i].place(x=3 * i + 1, y=res[len(res) - 1])
            bucket_sort_Canv.update()
            #print res
    return res


def bucket_sort_func():
    bucket_sort_Canv = Tk()
    bucket_sort_Canv.title("桶排序")
    bucket_sort_Canv.geometry('2400x1200')
    bucket_sort_Canv.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(bucket_sort_Canv, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义

    # 打印画布
    # for l in range(num - 1):
    #    divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)

    # 开始对随机数进行排序
    time_start = time.time()
    random_set = bucket_sort(random_set, bucket_sort_Canv, divide_set)
    time_end = time.time()

    time_used = "%.5f" % float(time_end - time_start)

    #  花费时间
    print time_used
    # 耗时展示
    time_lable = Label(bucket_sort_Canv, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # select_sort_func循环打开
    bucket_sort_Canv.update()
    bucket_sort_Canv.mainloop()
    return


def heap_sort_func():
    heap_sort_func = Tk()
    heap_sort_func.title("堆排序")
    heap_sort_func.geometry('2400x1200')
    heap_sort_func.resizable(width=True, height=True)
    # 关键字的获取
    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []  # 随机数集合
    divide_set = []  # 画布集合
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 产生 num 个从0到num_range的数
        divide_set.append("Cra_" + str(i))  # 产生num个画布
        divide_set[i] = Canvas(heap_sort_func, width=1, height=1100, background="#82b6d2")  # 给每个画布对象进行定义
    # 开始对随机数进行排序

    time_start = time.time()
    random_set = HeapSort(random_set, heap_sort_func, divide_set)
    time_end = time.time()

    time_used = "%.5f" % float(time_end - time_start)

    # 打印画布
    for l in range(num - 1):
        divide_set[l].place(x=3 * l + 1, y=random_set[l], anchor=NW)
    #  花费时间
    print time_used
    # 耗时展示
    time_lable = Label(heap_sort_func, text="排序耗时:" + str(time_used), width=20, height=1, bg="white")
    time_lable.pack(side=LEFT, anchor=N)
    # select_sort_func循环打开
    heap_sort_func.mainloop()
    return


def random_num():
    random_num = Tk()
    random_num.title("随机数列排序器")
    random_num.geometry('2400x1200')
    random_num.resizable(width=True, height=True)
    # random_num_frm_1 = Frame(random_num)
    # Button(random_num, text="random num", command=random_num, bg="#8b90de", fg="black").place(x=0, y=0, width=130, height=30)
    # random_num_frm_1.place(x=0, y=10, width=50, height=30)
    Button(random_num, text="快速排序(动态化)".decode('utf8').encode('utf8'), command=quick_sort_func, bg="#82b6d2",
           fg="black").place(x=120, y=0, width=130, height=30)
    # random_num_frm_1.place(x=100, y=10, width=50, height=30)
    Button(random_num, text="希尔排序(未动态化)".decode('utf8').encode('utf8'), command=sheel_sort_func, bg="#7dccc2",
           fg="black").place(x=340, y=0, width=130, height=30)
    # random_num_frm_1.place(x=200, y=10, width=10, height=5)
    Button(random_num, text="冒泡排序(动态化)".decode('utf8').encode('utf8'), command=maopao_sort_func, bg="#72cb95",
           fg="black").place(x=560, y=0, width=130, height=30)
    # random_num_frm_1.place(x=300, y=10, width=10, height=5)
    Button(random_num, text="归并排序(动态化)".decode('utf8').encode('utf8'), command=guibing_sort_func, bg="#a1c66e",
           fg="black").place(x=780, y=0, width=130, height=30)
    # random_num_frm_1.place(x=50, y=10, width=10, height=5)
    Button(random_num, text="选择排序(未动态化)".decode('utf8').encode('utf8'), command=select_sort_func, bg="#c3c86e",
           fg="black").place(x=1000, y=0, width=130, height=30)
    # random_num_frm_1.place(x=60, y=10, width=10, height=5)
    Button(random_num, text="插入排序(未动态化)".decode('utf8').encode('utf8'), command=insert_sort_func, bg="#caa86b",
           fg="black").place(x=1220, y=0, width=130, height=30)
    # random_num_frm_1.place(x=70, y=10, width=10, height=5)
    Button(random_num, text="基数排序(动态化)".decode('utf8').encode('utf8'), command=bucket_sort_func, bg="#c97862",
           fg="black").place(x=1440, y=0, width=130, height=30)
    # random_num_frm_1.place(x=80, y=10, width=10, height=5)
    Button(random_num, text="堆排序(动态化)".decode('utf8').encode('utf8'), command=heap_sort_func, bg="#4fcc73",
           fg="black").place(x=1660, y=0, width=130, height=30)
    # random_num_frm_1.place(x=90, y=10, width=10, height=5)

    num = NUM.get()
    num_range = RANGE.get()
    color_list = ["#3cb968", "#6bc545", "#b7c741", "#7f49ca", "#c541b5", "#c54164", "#c5c241", "#c56041"]
    random_set = []
    divide_set = []
    for i in range(num + 1):
        random_set.append(random.randint(0, num_range))  # 生成随机数列
        divide_set.append("frm_" + str(i))
        divide_set[i] = Canvas(random_num, width=1, height=1100, background="#82b6d2")
    # random_set.sort()
    for j in range(num - 1):
        # divide_set[j].create_text(2, 1200, text=random_set[j])
        divide_set[j].place(x=3*j+1, y=1200 - random_set[j], anchor=NE)
    random_num.mainloop()


# 提示文字
frm_input_text = Frame(sort)
Label(frm_input_text, text="取值范围1~".decode('utf8').encode('utf8')).pack(fill="y", expand="yes")
Label(frm_input_text, text="数据数量".decode('utf8').encode('utf8')).pack(fill="y", expand="yes")
frm_input_text.pack(side=LEFT, anchor=N)

# 输入排序数范围
frm_range_count = Frame(sort)
RANGE = IntVar()
e_range = Entry(frm_range_count, textvariable=RANGE).pack()

# 输入排序数数量
NUM = IntVar()
e_num = Entry(frm_range_count, textvariable=NUM).pack()
frm_range_count.pack(side=LEFT, anchor=N)

# 按钮
frm_main_botton = Frame(sort)
Button(frm_main_botton, text="产生随机数", command=random_num).pack(ipady=9)
frm_main_botton.pack(side=LEFT, anchor=N)

# 背景色
frm_bgcolor = Label(sort, width=300, height=200, background="black")
frm_bgcolor.pack(side=BOTTOM)

# 其他
frm_input_other = Frame(sort, width=200, height=100)
# Label(frm_input_text, text="完成时间 ".decode('utf8').encode('utf8'), bg="white").pack(fill="y", expand="yes")
# Label(frm_input_text, text="作者@汪俊雄".decode('utf8').encode('utf8'), bg="blue").pack()
# Label(frm_input_text, text="指导老师@张华".decode('utf8').encode('utf8'), bg="red").pack()
# Label(frm_input_text, text="哈尔滨工业大学(威海)".decode('utf8').encode('utf8'), bg="green").pack()
frm_input_other.pack(side=BOTTOM, anchor=S)
# 图片
# image = Image.open("G:\\WUD\\software_development_and_designii\\sort\\sort.gif")
# img = ImageTk.PhotoImage(image)
# image_label = Label(sort, image=img)
# image_label.pack(side=BOTTOM, anchor=SE)
sort.mainloop()

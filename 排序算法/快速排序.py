'''
快速排序是对冒泡排序的一种改进
两种解决方案
1、从两头向中间找
2、从前向后单向查找
'''
#         0    1   2   3
#list1 = [12 , 43 , 9 , 3 , 4 , 21 , 23 ,34 , 2 , 5 , 7]

#找到
#根据某个值将列表一分为2，对分开的两个列表重复以上操作
num = 0
def quick_sort(lst,begin,end):
    global num
    if begin >= end :#如果起始位置不比结束位置小，则已排序完成
        return
    key = lst[begin] #给key赋值，后面和key比较
    i = begin #i在起始位置
    for j in range(begin + 1,end + 1):
        if lst[j] < key : #如果发现比key小的值
            #使用i后面一个位置的元素和lst[j]交换
            i += 1
            lst[j],lst[i] = lst[i],lst[j] #小元素换位
            num += 1
    lst[begin],lst[i] = lst[i],lst[begin] #将begin位置的数据挪到后面i的位置

    print(lst)

    quick_sort(lst,begin,i - 1)
    quick_sort(lst,i + 1,end)
list1 = [1,1,1,1,1,1]  # 测试排序算法是否为稳定排序
begin = 0
end = len(list1) - 1
print('排序前:\n',list1,sep = '')

#print('第1次快速排序后：',end = '')#比12小的数据都到12前面去了
quick_sort(list1,begin,end)
# print('num:',num)


'''
print('第2次快速排序后：',end = '')#比12小的数据都到12前面去了
quick_sort(list1,begin,end)

print('第3次快速排序后：',end = '')#比12小的数据都到12前面去了
quick_sort(list1,begin,end)
'''


#         0    1   2   3
#list1 = [12 , 43 , 2 , 5 ]



'''
# 使用列表推导式实现快速排序找到标准点，将列表分为两部分，小的放在前面，大的放在后面
def sortKu(ls):
    # print(ls)
    if len(ls) <= 1:
        return ls
    return sortKu([i for i in ls[1:] if i < ls[0]]) + ls[0:1] + sortKu([i for i in ls[1:] if i >= ls[0]])

lst = [53,412,431,87,5,6,4,233,7]
print(sortKu(lst))
'''


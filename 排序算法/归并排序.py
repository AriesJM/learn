#归并排序,一步步分析，还没太懂
'''
归并排序原理：
1、初始时，将待排序序列中的n个记录看做是n个有序子序列
2、把当时序列组里的有序子序列两两归并，完成一遍序列组里的排序序列个数减半，每个序列的长度加倍
3、对加长的有序序列重复上面的操作，最终得到一个长度为n的有序序列
这种归并方法为二路归并排序，还有三路归并排序和多路归并排序

归并排序操作过程中对数据的访问具有局部性，适合外存数据交换的特点，特别适合处理一组记录形成的数据块
由于这些情况，归并排序适合于处理存储在外存的大量数据


归并排序分为三层，每层负责不同的工作
1、最下层：实现表中相邻的一对有序序列的归并工作，将归并的结果存入另一个顺序表里相同的位置
2、中间层：基于操作一（一对序列的归并操作），实现对整个表里顺序各对有序序列的归并，完成一遍归并，
对序列的归并结果顺序存入另一个顺序表里的同位置分段
3、最高层：在两个顺序表之间往复执行操作2，完成一遍归并后交换两个表的地位，然后重复2的工作，
直到整个表中只有一个有序序列

'''
lst = [21,43,6,3,7,31,43,23]


def merge(lfrom,lto,low,mid,high):
    '''
    功能：完成表中连续排放的两个有序序列的归并工作
    :param lfrom:将lfrom中的数据归并到lto中，
    :param lto:将归并的结果放到lto中
    :param low:需要归并的序列分别是lfrom[low:mid],lfrom[mid:high]
    :param mid:
    :param high:
    :return:None
    '''
    i,j,k = low,mid,low
    while i < mid and j < high: #反复复制分段首记录中较小的
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else :
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:              #复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:             #复制第二段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom,lto,llen,slen):
    '''
    功能：归并长为slen的两段序列
    :param lfrom: 要归并的序列
    :param lto: 归并后存放的序列
    :param llen: 开始归并时分段长度，
    :param slen: 整个表的长度
    :return:None
    '''
    i = 0
    while i + 2 * slen < llen:  #归并长slen的两段
        merge(lfrom , lto , i , i + slen , i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:         #剩下两段，后段长度小于slen
        merge(lfrom,lto,i,i + slen,llen)
    else :                      #只剩下一段，复制到lto
        for j in range(i,llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    '''
    功能：创建另一个长度相同的表，然后在两个表中往复做一遍遍的归并
    :param lst: 要排序的列表
    :return:None
    '''
    slen,llen = 1,len(lst)
    #创建另一个长度相同的列表
    templst = [None]*llen
    while slen < llen :
        merge_pass(lst,templst,llen,slen)
        slen *= 2
        merge_pass(templst,lst,llen,slen)#结果存回原位
        slen *= 2



print('开始：',lst)
merge_sort(lst)
print('结束：',lst)







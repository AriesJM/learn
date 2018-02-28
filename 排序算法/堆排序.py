'''
- 什么是堆
	- 在这里首先要先解释一下什么是堆，堆栈是计算机的两种最基本的数据结构。
	- 堆的特点就是FIFO(first in first out)先进先出，
	- 堆在接收数据的时候先接收的数据会被先弹出。
	- 栈的特性正好与堆相反，是属于FILO(first in/last out)先进后出的类型。
	- 栈处于一级缓存而堆处于二级缓存中。

- 堆节点的访问
	- 通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中
	- (1)父节点i的左子节点在位置(2*i+1);
	- (2)父节点i的右子节点在位置(2*i+2);
	- (3)子节点i的父节点在位置floor((i-1)/2);

- 堆操作
	- 堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作:
	- (1)最大堆调整(MAX_Heapify):将堆的末端子节点作调整，使得子节点永远小于父节点。
	- 这是核心步骤，在建堆和堆排序都会用到。比较i的根节点和与其所对应i的孩子节点的值。
	- 当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，
	- 当i根节点的值比右孩子的节点所对应的值要小的时候，就把i根节点和右孩子节点所对应的值交换。
	- 然后再调用堆调整这个过程，可见这是一个递归的过程。
	- (2)建立最大堆(Build_Max_Heap):将堆所有数据重新排序。
	- 建堆的过程其实就是不断做最大堆调整的过程，
	- 从len/2出开始调整，一直比到第一个节点。
	- (3)堆排序(HeapSort):移除位在第一个数据的根节点，并做最大堆调整的递归运算。
	- 堆排序是利用建堆和堆调整来进行的。首先先建堆，然后将堆的根节点选出与最后一个节点进行
	- 交换，然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，
	- 对于n个数我们只需要做n-1次操作。
'''

def MAX_Heapify(heap,HeapSize,root):# 在堆中做结构调整使得父节点的值大于子节点，递归调整
    '''
    将列表看做树状结构，左节点位置等于2*root+1,右节点等于left+1,larger 最大值应该是父节点
    :param heap:
    :param HeapSize:
    :param root:
    :return:
    '''
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    # 如果最大值不是父节点，就要将父节点和子节点交换位置
    if larger != root:# 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)


def Build_MAX_Heap(heap):# 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)# 将堆的长度当独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):# 从后往前出数
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):# 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    # 遍历时是从后向前遍历，就是从数的叶节点向上递归
    for i in range(len(heap)-1,-1,-1):
    	# 这里为什么要交换，暂时没搞清楚
        heap[0],heap[i] = heap[i],heap[0] 
        MAX_Heapify(heap, i, 0) #  调整使得父节点的值大于子节点
    return heap


#  将列表看做是树状结构，递归调整使得父节点
#  		21 
#  	43		6
#  3  7 	  31  43
#23
lst = [21,43,6,3,7,31,43,23]
print('排序前：',lst)
HeapSort(lst)
print('排序后：',lst)




#依次选择数据，
'''
1、选择最小的
2、选择余下数据最小的放到第二个元素位置
3、时间复杂度是固定的O(n**2)
'''


list1 = [2,4,3,21,3,5435,43,543432,42,1]

for i in range(len(list1)):
    for n in range(i + 1 ,len(list1)) :
        if list1[n] < list1[i] :
            list1[i],list1[n] =  list1[n],list1[i]
print(list1)



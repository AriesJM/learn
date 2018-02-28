#插入排序,一次比较前面的数据，插入大的值前面，中间的值向后移动

'''
list1 = [14,3,24,3]
取出list1[1],和第0个比较，如果小于第0个就放在0的位置，如果大于第0个就放在第一个位置，
注意后面的元素是否需要向后移动
'''

list1 = [14,3,2,7,4,2,9,33,44,83,17,24,24,5]
for i in range(1,len(list1)) :
    #去比较0~i-1的数字，如果小于第n个元素，就放在n前面的位置
    for n in range(0,i) :
        #需要从list1[n]到list1[i - 1]都要向后移动，list1[i]->list1[n]
        if list1[i] < list1[n] :
            x = list1[i]
            for j in range(i,n,-1):
                list1[j] = list1[j - 1]
            list1[n] = x
            print('     ',list1[i] ,'>', list1[n],'两者进行交换')
    print('交换完',list1[i],'后当前list1为：',list1)
    print('**********第',i,'个数比较完')







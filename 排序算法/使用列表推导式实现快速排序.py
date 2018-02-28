# 找到标准点，将列表分为两部分，小的放在前面，大的放在后面
def sortKu(ls):
    # print(ls)
    if len(ls) <= 1:
        return ls
    return sortKu([i for i in ls[1:] if i < ls[0]]) + ls[0:1] + sortKu([i for i in ls[1:] if i >= ls[0]])

lst = [53,412,431,431,431,87,5,87,6,4,233,7]
print(sortKu(lst))




list2 = []
list1 = [1,2,3,4]
for i in list1:
    for j in list1:
        for k in list1:
            #列表的添加元素是有序添加的，因此三个数的组合久完全组合出来达成要求：互不相同
            #再通过判断三个数中是否有两两相等的情况，有就不添加，没有才添加，达成要求：无重复数字
            if i==j or i==k or j==k:
                continue
            else:
                list2.append(str(i)+str(j)+str(k))
# print(list3)
print(list2)

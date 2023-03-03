def isSorted(l):
    flag = 0
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            flag = 1
        i += 1
    if not flag:
        return True
    else:
        return False


l1 = [1,1,2,3,4]
l2 = [x for x in range(10)]
l3 = [x for x in range(0,10,-1)]
l4 = [1,3,2,1]

print("L1 : {}\nL2 : {}\nL3 : {}\n".format(isSorted(l1),isSorted(l2),isSorted(l3)))
print("L4 : {}".format(isSorted(l4)))  


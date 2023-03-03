def hasDupclicate(l):
    new_list = []
    flag = 0
    for i in l:
        if i in new_list:
            flag = 1

        new_list.append(i)
    if not flag:
        return False
    else:
        return True

l1 = [1,4,9,10,23]
l2 = [1,4,9,9,23]

print(hasDupclicate(l1))
print(hasDupclicate(l2))


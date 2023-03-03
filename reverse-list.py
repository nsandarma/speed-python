l1 = [i for i in range(1,15,2)]

#cara simple dengan metode slicing list
print(l1[::-1])


# cara ribet nya, hehe
def reverse(l):
    length = len(l)
    new_list = [None]*length
    for i in l:
        length -= 1
        new_list[length] = i
    print(new_list)


reverse(l1)


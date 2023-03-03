# Cara Pertama
def findMaximum(l):
    max_values = None
    position = None
    for i,v in enumerate(l):
        if max_values is None or v > max_values:
            max_values = v
            position = i
    print("max values is : {} and position is : {}".format(max_values,position))


# Cara Kedua 
def findMaximum2(l):
    maximum = l[0]
    index = 0
    for i,v in enumerate(l):
        if v > maximum:
            maximum=v
            index = i
    print('Max : {} and Position : {}'.format(maximum,index))
    
if __name__ == "__main__":
    i = [2,1,4,2,5,2,1]
    findMaximum(i)
    findMaximum2(i)

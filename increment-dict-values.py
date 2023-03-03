def updateAges(ages,n):
    for i in ages:
        ages[i] += n
    print(ages)


student = {'peter':10,
            'isabel':11,
           'anna':9,
           'thomas':10,
           'bob':10,
           'joseph':11,
           'maria':12,
           'gabriel':10
           }

updateAges(student,1)

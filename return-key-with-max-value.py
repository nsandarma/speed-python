# Cara pertama Manual :3
def oldestStudent(ages):
    maximum = list(ages.values())[0]
    names = None
    for i in ages:
        if ages[i] > maximum:
            maximum = ages[i]
            names = i
    print("names {} is {}".format(names,maximum))

# Cara kedua menggunakan module max()
def oldestStudent2(ages):
    value = list(ages.values())
    key = list(ages.keys())
    print(f"names {key[value.index(max(value))]} is {max(value)}")

    
student = {'peter':10,
            'isabel':11,
           'anna':9,
           'thomas':10,
           'bob':10,
           'joseph':11,
           'maria':12,
           'gabriel':10
           }

oldestStudent(student)
oldestStudent2(student)

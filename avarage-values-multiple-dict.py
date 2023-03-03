def calculateAvarageAge(students):
    ages = sum([students[i]['age'] for i in students])/len(students)
    print(ages)
 
def findStudents(address,students):
    names = [i for i in students if students[i]['address'] == address]
    print(names)


students = {
        "peter":{'age':10,'address':"Lisbon"},
        "susan":{'age':11,'address':'Sweden'},
        'charles':{'age':9,'address':'Turkey'},
        'thomas':{'age':10,'address':'Lisbon'}
        }

calculateAvarageAge(students)
findStudents('Lisbon',students)

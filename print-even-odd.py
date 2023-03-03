# Cara pertama
def printEvenOdd(n):
    while n > 0:
        if n % 2 == 0:
            print("Even number:",n)
        else:
            print("Odd number:",n)
        n -= 1


# Cara kedua

n = 10
for i in range(n,0,-1):
    result = "Even" if i % 2 == 0 else "Odd"
    print(f"{result} number:{i}")

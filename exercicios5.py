def numeros():
    x = 1
    while x<=100: 
        print(x)
    x = x + 1
#numeros

def numeros1():
    x = 50
    while x<=100: 
        print(x)
    x = x + 1
#numeros1

def numeros2():
    x = 10
    while x>=0: 
        print(x)
    x = x - 1
#numeros2

def numeros3():
    fim = int(input("Digite o último número a imprimir:"))
    x = 0
    while x <= fim:
        if x % 2 == 0:
            print(x)
        x = x + 1
#numeros3()

def numeros4():
    fim = int(input("Digite o último número a imprimir:"))
    x = 0
    while x <= fim:
        if x % 2 == 1:
            print(x)
        x = x + 1
#numeros4()

def tabuada():
    n = int(input("Tabuada de: "))
    x = 1 
    while x <= 10:
        print(n*x)
        x = x+1
tabuada()
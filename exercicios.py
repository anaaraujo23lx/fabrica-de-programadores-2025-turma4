def quadrado():
    lado = int(input("Digite o valor do lado: "))
    area = lado**2 # lado*lado
    print(area)
#quadrado()

def salario():
    salario = int(input("Digite o valor do salario atual"))
    reajuste = (15/100*salario) + salario
    print(reajuste)
#salario()

def triangulo():
    lado = int(input("Digite o valor do lado"))
    area = (lado*lado)/2
    print(area)
#triangulo()

def celsius():
    graus_celsius = int(input("Digite a temperatura °C"))
    fahrenheit = (9*graus_celsius+160)/5
    print( fahrenheit)
#celsius()



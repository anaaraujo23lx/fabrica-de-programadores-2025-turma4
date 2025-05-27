'''
numero_string = input("Digite um numero: ")
numero_inteiro = int(numero_string)
subtraçao = numero_inteiro - 2

'''

numero_um = int(input("Numero um"))
numero_dois = int(input("Numero dois"))
resultado_soma = numero_um / numero_dois
resultado_soma_texto = str(resultado_soma)
mensagem = "O resultado da soma é: "+ resultado_soma_texto


print(mensagem)

'''

numero = 10

def apresentar_numero(): 
    global numero
    print(numero)
    numero = 15
    print(numero)

apresentar_numero()
print(numero)

'''
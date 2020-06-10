n1= float(input("Digite um numero: "))
n2= float(input("Digite um numero: "))
operador= int(input("Qual operação?"))
def mat(a,b):
    if operador == 0:
        return a+b
    elif operador == 1:
        return a-b
    elif operador == 2:
        return a*b
    elif operador == 3:
        return a/b

print(mat(n1,n2))
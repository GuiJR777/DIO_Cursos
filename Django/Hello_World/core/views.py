from django.shortcuts import render, HttpResponse



# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1>Hello {}!!<h1>'.format(nome))

def soma(request, n1, n2):
    soma= int(n1)+int(n2)
    return HttpResponse('A soma de {} e {} é {}'.format(n1, n2, soma))
def sub(request, n1, n2):
    sub= int(n1)-int(n2)
    return HttpResponse('A subtração de {} e {} é {}'.format(n1, n2, sub))
def mult(request, n1, n2):
    mult= int(n1)*int(n2)
    return HttpResponse('A multiplicação de {} e {} é {}'.format(n1, n2, mult))
def div(request, n1, n2):
    div= int(n1)/int(n2)
    return HttpResponse('A divisão de {} e {} é {}'.format(n1, n2, div))
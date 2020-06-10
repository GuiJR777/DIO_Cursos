import shutil
# def criar_arquivo(texto):
#     arquivo= open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()
# def atualizar_arquivo(texto):
#     arquivo= open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

# def ler_arquivo(nome_arquivo):
#     arquivo= open(nome_arquivo, 'r')
#     texto= arquivo.read()
#     print(texto)


# if __name__ == "__main__":
#     #criar_arquivo('Primeira linha\n')
#     #atualizar_arquivo("Quarta linha\n")
#     ler_arquivo('teste.txt')

def media_notas(nome_arquivo):
    arquivo= open(nome_arquivo, 'r')#abre arquivo
    aluno_nota= arquivo.read()#le arquivo
    aluno_nota= aluno_nota.split('\n')#Transforma as informações em lista separando na quebra de linha
    lista_media=[]
    for x in aluno_nota:
        lista_notas= x.split(',')
        aluno= lista_notas[0]
        lista_notas.pop(0)
        media= lambda notas: sum([int(i) for i in notas])/len(lista_notas)
        lista_media.append({aluno:media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    NewName= str(input('Que nome quer dar a seu arquivo? '))
    shutil.copy(nome_arquivo, 'C:/Users/ULTRABOOK/Desktop/'+ NewName)

if __name__ == "__main__":
    # lista_media= media_notas('notas.txt')
    # print(lista_media)
    copia_arquivo('notas.txt')
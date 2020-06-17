import requests

def retorna_rua_cep():
    cep= int(input('Digite um Cep: '))
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))#api que retorna dados de ceps
    # print(response.status_code)
    # print(response.json())
    dados_cep= response.json()
    rua= dados_cep['logradouro']
    print(rua)

def retorna_infos_pokemon():
    pokemon= str(input('Digite o nome de um pokemon para saber mais: '))
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon= response.json()
    print(dados_pokemon['sprites'])



if __name__ == "__main__":
    # retorna_rua_cep()
    #retorna_infos_pokemon()
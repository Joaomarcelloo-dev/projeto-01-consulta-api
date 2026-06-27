
import requests

def limpar_cep(cep_bruto): 
    cep_limpo = cep_bruto.replace('-', '').replace(' ', '')
    if len(cep_limpo) == 8 and cep_limpo.isdigit():
        return cep_limpo
    else:
        return None

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        return dados 
    except requests.exceptions.RequestException:
        return None 

def exibir_endereco(dados):
    rua = dados ['logradouro']
    bairro = dados['bairro']
    cidade = dados['localidade']
    estado = dados['uf']

    print('\n--- Endereço encontrado ---')
    print(f'Rua:   {rua}')
    print(f'Bairro:   {bairro}')
    print(f'Cidade:  {cidade} - {estado}')

print('=== Consulta de Cep ===')
print('Digite "sair" para encerrar.\n')

while True:
    entrada = input("Digite o CEP: ")

    if entrada == "sair":
        print("Até logo!")
        break

    cep = limpar_cep(entrada)
    if cep is None:
        print("Formato inválido. O CEP deve ter 8 dígitos.\n")
        continue

    dados = consultar_cep(cep)
    if dados is None:
        print("Erro de conexão. Tente novamente.\n")
        continue

    if "erro" in dados:
        print("CEP não encontrado. Verifique o número e tente novamente.\n")
        continue

    exibir_endereco(dados)
    print()
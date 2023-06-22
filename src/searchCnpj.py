def Cnpj(clear, requests, cia, ba, Enter):
    clear()
    cnpj = input(f'{cia}DIGITE O CNPJ{ba}: ')
    data = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').json()
    clear()
    print(f'''
{cia}NOME{ba}: {data["nome"]}
{cia}COMPLEMENTO{ba} : {data["complemento"]}
{cia}ATUALIZACAO CADASTRAL{ba}: {data["data_situacao"]}
{cia}TIPO{ba}: {data["tipo"]}
{cia}TELEFONE{ba}: {data["telefone"]}
{cia}EMAIL{ba}: {data["email"]}
{cia}SITUACAO{ba}: {data["situacao"]}
{cia}BAIRRO{ba}: {data["bairro"]}
{cia}NUMERO{ba}: {data["numero"]}
{cia}CEP{ba}: {data["cep"]}
{cia}MUNICIPIO{ba}: {data["municipio"]}
{cia}DATA DE ABERTURA{ba}: {data["abertura"]}
{cia}CNPJ{ba}: {data["cnpj"]}
{cia}CAPITAL SOCIAL{ba}: {data["capital_social"]}
''')
    Enter()
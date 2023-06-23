def Cnpj(clear, requests, cian, ba, restartCode):
    clear()
    cnpj = input(f'{cian}DIGITE O CNPJ{white}: ')
    data = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').json()
    clear()
    print(f'''
{cian}NOME{white}: {data["nome"]}
{cian}COMPLEMENTO{white} : {data["complemento"]}
{cian}ATUALIZACAO CADASTRAL{white}: {data["data_situacao"]}
{cian}TIPO{white}: {data["tipo"]}
{cian}TELEFONE{white}: {data["telefone"]}
{cian}EMAIL{white}: {data["email"]}
{cian}SITUACAO{white}: {data["situacao"]}
{cian}BAIRRO{white}: {data["bairro"]}
{cian}NUMERO{white}: {data["numero"]}
{cian}CEP{white}: {data["cep"]}
{cian}MUNICIPIO{white}: {data["municipio"]}
{cian}DATA DE ABERTURA{white}: {data["abertura"]}
{cian}CNPJ{white}: {data["cnpj"]}
{cian}CAPITAL SOcianL{white}: {data["capital_socianl"]}
''')
    restartCode()
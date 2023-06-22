def Cep(clear, requests, cia, ba, Enter):
    clear()
    cep = input(f'{cia}DIGITE O CEP{ba}: ')
    data = requests.get(f'https://viacep.com.br/ws/{cep}/json').json()
    clear()
    print(f'''
{cia}CEP{ba}: {data["cep"]}
{cia}LOGRADOURO{ba}: {data["logradouro"]}
{cia}COMPLEMENTO{ba}: {data["complemento"]}
{cia}BAIRRO{ba}: {data["bairro"]}
{cia}LOCALIDADE{ba}: {data["localidade"]}
{cia}UF{ba}: {data["uf"]}
{cia}IBGE{ba}: {data["ibge"]}
{cia}GIA{ba}: {data["gia"]}
{cia}DDD{ba}: {data["ddd"]}
{cia}SIAF{ba}: {data["siafi"]}
''')
    Enter()
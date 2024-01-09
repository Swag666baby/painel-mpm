def Cep(clear, requests, cian, white, restartCode):
    clear()
    cep = input(f'{cian}DIGITE O CEP{white}: ')
    data = requests.get(f'https://viacep.com.br/ws/{cep}/json').json()
    clear()
    print(f'''
{cian}CEP{white}: {data["cep"]}
{cian}LOGRADOURO{white}: {data["logradouro"]}
{cian}COMPLEMENTO{white}: {data["complemento"]}
{cian}BAIRRO{white}: {data["bairro"]}
{cian}LOCALIDADE{white}: {data["localidade"]}
{cian}UF{white}: {data["uf"]}
{cian}IBGE{white}: {data["ibge"]}
{cian}GIA{white}: {data["gia"]}
{cian}DDD{white}: {data["ddd"]}
{cian}SIAF{white}: {data["siafi"]}
''')
    restartCode()

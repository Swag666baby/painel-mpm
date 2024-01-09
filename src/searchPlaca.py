def Placa(clear, requests, cian, white, restartCode):
    clear()
    placa = input(f'{cian}DIGITE A PLACA{white}: ')
    data = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).json()
    clear()
    print(f'''
{cian}ANO{white}: {data["ano"]}
{cian}ANO MODELO{white}: {data["anoModelo"]}
{cian}COR{white}: {data["cor"]}
{cian}CHASSI{white}: {data["chassi"]}
{cian}CODIGO DE RETORNO{white}: {data["codigoRetorno"]}
{cian}CODIGO DE SITUACAO{white}: {data["codigoSituacao"]}
{cian}DATA{white}: {data["data"]}
{cian}DATA FURTO{white}: {data["dataAtualizacaoRouboFurto"]}
{cian}MARCA{white}: {data["marca"]}
{cian}MODELO{white}: {data["modelo"]}
{cian}LOCALIDADE{white}: {data["uf"]}
{cian}PLACA{white}: {data["placa"]}
{cian}SITUACAO{white}: {data["situacao"]}
{cian}MUNICIPIO{white}: {data["municipio"]}
{cian}RETORNO{white}: {data["mensagemRetorno"]}
''')
    restartCode()

def Placa(clear, requests, cia, ba, Enter):
    clear()
    placa = input(f'{cia}DIGITE A PLACA{ba}: ')
    data = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).json()
    clear()
    print(f'''
{cia}ANO{ba}: {data["ano"]}
{cia}ANO MODELO{ba}: {data["anoModelo"]}
{cia}COR{ba}: {data["cor"]}
{cia}CHASSI{ba}: {data["chassi"]}
{cia}CODIGO DE RETORNO{ba}: {data["codigoRetorno"]}
{cia}CODIGO DE SITUACAO{ba}: {data["codigoSituacao"]}
{cia}DATA{ba}: {data["data"]}
{cia}DATA FURTO{ba}: {data["dataAtualizacaoRouboFurto"]}
{cia}MARCA{ba}: {data["marca"]}
{cia}MODELO{ba}: {data["modelo"]}
{cia}LOCALIDADE{ba}: {data["uf"]}
{cia}PLACA{ba}: {data["placa"]}
{cia}SITUACAO{ba}: {data["situacao"]}
{cia}MUNICIPIO{ba}: {data["municipio"]}
{cia}RETORNO{ba}: {data["mensagemRetorno"]}
''')
    Enter()
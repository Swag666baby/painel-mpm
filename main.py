#cia = '\033[1;36m'
#gabriel é homossexual
cl = '\033[0m'
az = '\033[1;94m'
cia = '\033[1;36m'
ba = '\033[1;37m'

import requests
import os
from sys import argv, executable
import base64


def restart():
    os.execl(executable, executable, *argv)

def Enter():
    input("Pressione ENTER para continuar")
    
    restart()

def clear():
    os.system('cls||clear')
    

def opcoes():
    
    
    print(f'   {ba}━━━━━━━━❮◆❯━━━━━━━━━━{ba}')
    print('    {}MILICIA PIKA DE MEL\033[0m'.format(cia))
    print(f'{ba}   ━━━━━━━━❮◆❯━━━━━━━━━━{ba}')
    print('\033[1;37mCRIADO POR: SWAG,MRDINIZ,SPYWARE,INSTATOS\033[0;0m')
    print('')
    print('\033[1;37mGITHUB: Swag666baby // Spyware0 // mrdiniz88\033[m')
    print(f'{ba}ZAP: 556295598220')
    print(' ')
    print(f'{ba}ESCOLHA UM NÚMERO: ')
    print(' ')
    print('{}━❮{}1{}❯━{} CONSULTA DE CEP'.format(ba,cia,ba,cia))
    print('{}━❮{}2{}❯━{} CONSULTA DE IP'.format(ba,cia,ba,cia))
    print('{}━❮{}3{}❯━{} CONSULTA DE CNPJ'.format(ba,cia,ba,cia))
    print('{}━❮{}4{}❯━{} CONSULTA DE PLACA'.format(ba,cia,ba,cia))
    
    opc = input('➣➣➣    {}'.format(cl))

    if opc == '1':
    	Cep()

    elif opc == '2':
    	Ip()

    elif opc == '3':
    	Cnpj()
    	
    elif opc == '4':
    	placa()
    	
    else:
        restart()


def Ip():
    clear()

    ip = input('DIGITE O IP: ')
 
    r = requests.get(f'https://ipwhois.app/json/{ip}')
    data = r.json()
    clear()
    print(f'{cia}IP{ba}: {data["ip"]}')
    print(f'{cia}CONTINENTE{ba}: {data ["continent"]}')
    print(f'{cia}PAIS{ba}: {data ["country"]}')
    print(f'{cia}CAPITAL{ba}: {data ["country_capital"]}')
    print(f'{cia}CODIGO DE AREA{ba}: {data ["country_phone"]}')
    print(f'{cia}ESTADO{ba}: {data ["region"]}')
    print(f'{cia}LATITUDE{ba}: {data ["latitude"]}')
    print(f'{cia}LONGITUDEDE{ba}: {data ["longitude"]}')
    print(f'{cia}PROVEDOR{ba}: {data ["asn"]}')
    Enter()


def Cep():
    clear()

    cep = input('DIGITE O CEP: ')
    a = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    cp = a.json()
    clear()
    print(f'{cia}CEP{ba}: {cp["cep"]}')
    print(f'{cia}LOGRADOURO{ba}: {cp["logradouro"]}')
    print(f'{cia}COMPLEMENTO{ba}: {cp["complemento"]}')
    print(f'{cia}BAIRRO{ba}: {cp["bairro"]}')
    print(f'{cia}LOCALIDADE{ba}: {cp["localidade"]}')
    print(f'{cia}UF{ba}: {cp["uf"]}')
    print(f'{cia}IBGE{ba}: {cp["ibge"]}')
    print(f'{cia}GIA{ba}: {cp["gia"]}')
    print(f'{cia}DDD{ba}: {cp["ddd"]}')
    print(f'{cia}SIAF{ba}: {cp["siafi"]}')
    Enter()

def Cnpj():
    clear()
    cnpj = input('DIGITE O CNPJ: ')
	
    b = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
	
    pj = b.json()
    
    clear()
	
    print(f'{cia}NOME{ba}: {pj["nome"]}')
    print(f'{cia}COMPLEMENTO{ba} : {pj["complemento"]}')
    print(f'{cia}ATUALIZACAO CADASTRAL{ba}: {pj["data_situacao"]}')
    print(f'{cia}TIPO{ba}: {pj["tipo"]}')
    print(f'{cia}TELEFONE{ba}: {pj["telefone"]}')
    print(f'{cia}EMAIL{ba}: {pj["email"]}')
    print(f'{cia}SITUACAO{ba}: {pj["situacao"]}')
    print(f'{cia}BAIRRO{ba}: {pj["bairro"]}')
    print(f'{cia}NUMERO{ba}: {pj["numero"]}')
    print(f'{cia}CEP{ba}: {pj["cep"]}')
    print(f'{cia}MUNICIPIO{ba}: {pj["municipio"]}')
    print(f'{cia}DATA DE ABERTURA{ba}: {pj["abertura"]}')
    print(f'{cia}CNPJ{ba}: {pj["cnpj"]}')
    print(f'{cia}CAPITAL SOCIAL{ba}: {pj["capital_social"]}')
    Enter()

def placa():
    clear()
    placa = input('DIGITE A PLACA: ')
	
    u = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False)
	
    pj = u.json()
    
    clear()

    
    print(f'{cia}ANO{ba}: {pj["ano"]}')
    print(f'{cia}ANO MODELO{ba}: {pj["anoModelo"]}')
    print(f'{cia}COR{cl}: {pj["cor"]}')
    print(f'{cia}CHASSI{ba}: {pj["chassi"]}')
    print(f'{cia}CODIGO DE RETORNO{ba}: {pj["codigoRetorno"]}')
    print(f'{cia}CODIGO DE SITUACAO{cl}: {pj["codigoSituacao"]}')
    print(f'{cia}DATA{ba}: {pj["data"]}')
    print(f'{cia}DATA FURTO{ba}: {pj["dataAtualizacaoRouboFurto"]}')
    print(f'{cia}MARCA{ba}: {pj["marca"]}')
    print(f'{cia}MODELO{ba}: {pj["modelo"]}')
    print(f'{cia}LOCALIDADE{ba}: {pj["uf"]}')
    print(f'{cia}PLACA{ba}: {pj["placa"]}')
    print(f'{cia}SITUACAO{ba}: {pj["situacao"]}')
    print(f'{cia}MUNICIPIO{ba}: {pj["municipio"]}')
    print(f'{cia}RETORNO{ba}: {pj["mensagemRetorno"]}')
    Enter()


clear()

opcoes()

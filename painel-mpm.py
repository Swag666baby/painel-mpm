az = '\033[1;94m'
cia = '\033[1;36m'
ba = '\033[1;37m'
ro = '\033[1;35m'
v = '\033[1;31m'

import requests, os, re, time
from sys import argv, executable

def restart():
    os.execl(executable, executable, *argv)

def Enter():
    input("enter para continuar")
    
    restart()
    
def tempo():
	time.sleep(0.5)

def clear():
    os.system('cls||clear')
    

def opcoes():
    
 
    
    print(f'{ba}      ━━━━━━━━❮◆❯━━━━━━━━━━{ba}\n        {cia}MILICIA PIKA DE MEL{ba}\n    {ba}  ━━━━━━━━❮◆❯━━━━━━━━━━{ba}\n  CRIADO POR: {ro}SWAG,MRDINIZ,SPYWARE{ba}\n  GITHUB: Swag666baby {cia}//{ba} mrdiniz88 {cia}//{ba} Spyware0 \n  ZAP: 556295598220\n\n  ESCOLHA UM NÚMERO: \n\n\n  {ba}━❮{cia}1{ba}❯━{cia} CONSULTA DE CEP\n  {ba}━❮{cia}2{ba}❯━{cia} CONSULTA DE IP\n  {ba}━❮{cia}3{ba}❯━{cia} CONSULTA DE CNPJ\n  {ba}━❮{cia}4{ba}❯━{cia} CONSULTA DE PLACA\n  {ba}━❮{cia}5{ba}❯━{cia} CONSULTA DE TELEFONE\n  {ba}━❮{cia}6{ba}❯━{cia} CONSULTA DE CPF\n  {ba}━❮{cia}7{ba}❯━{cia} CONSULTA DE NOME\n\n  {ba}━❮{cia}0{ba}❯━{v} EXIT{ba}')
    
    opc = input(f'{cia}   ➣➣➣    {ba}')
    

    if opc == '1':
    	Cep()

    elif opc == '2':
    	Ip()

    elif opc == '3':
    	Cnpj()
    	
    elif opc == '4':
    	placa()
    	
    elif opc == '5':
    	telefone()
    	
    elif opc == '6':
    	cpf()
    	
    elif opc == '7':
    	nome()
    elif opc == '0':
    	print('')
    	
    else:
        restart()


def Ip():
    clear()

    ip = input(f'{cia}DIGITE O IP{ba}: ')
 
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
    cep = input(f'{cia}DIGITE O CEP{ba}: ')
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
    cnpj = input(f'{cia}DIGITE O CNPJ{ba}: ')
	
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
    placa = input(f'{cia}DIGITE A PLACA{ba}: ')
	
    u = requests.get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False)
	
    pj = u.json()
    
    clear()

    print(f'{cia}ANO{ba}: {pj["ano"]}')
    print(f'{cia}ANO MODELO{ba}: {pj["anoModelo"]}')
    print(f'{cia}COR{ba}: {pj["cor"]}')
    print(f'{cia}CHASSI{ba}: {pj["chassi"]}')
    print(f'{cia}CODIGO DE RETORNO{ba}: {pj["codigoRetorno"]}')
    print(f'{cia}CODIGO DE SITUACAO{ba}: {pj["codigoSituacao"]}')
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
    
def telefone():
	clear()
	print(f'{v}OPÇÃO DESABILITADA{ba}')
	Enter()
	
def cpf():
	clear()
	print(f'{v}OPÇÃO DESABILITADA{ba}')
	Enter()
	
def nome():
	clear()
	print(f'{v}OPÇÃO DESABILITADA{ba}')
	Enter()

clear()

opcoes()

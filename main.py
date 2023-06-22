cian = '\033[1;36m'
white = '\033[1;37m'
purple = '\033[1;35m'
v = '\033[1;31m'

import requests, os, re, time
from sys import argv, executable, path
path.append(os.path.abspath("src"))
from searchIp import Ip
from searchCep import Cep
from searchCnpj import Cnpj
from searchPlaca import Placa

def restart():
    os.execl(executable, executable, *argv)

def Enter():
    input("Pressione ENTER para continuar")
    restart()
    
def tempo():
	time.sleep(0.5)

def clear():
    os.system('cls||clear')
    

def options():
    print(f'''      {white}━━━━━━━━❮◆❯━━━━━━━━━━{white}
        {cian}MILIcian PIKA DE MEL{white}
    {white}  ━━━━━━━━❮◆❯━━━━━━━━━━{white}
  CRIADO POR: {purple}SWAG,SPYWARE,DINIZ{white}
  GITHUB: Swag666baby {cian}//{white} Spyware0 {cian}//{white} mrdiniz88
    
  ESCOLHA UM NÚMERO: 
    

  {white}━❮{cian}1{white}❯━{cian} CONSULTA DE CEP
  {white}━❮{cian}2{white}❯━{cian} CONSULTA DE IP
  {white}━❮{cian}3{white}❯━{cian} CONSULTA DE CNPJ
  {white}━❮{cian}4{white}❯━{cian} CONSULTA DE PLACA''')
    
    choice = input(f'   ➣➣➣    {white}')

    if choice == '1':
        try:
            Cep(clear, requests, cian, white, Enter)
        except:
            print("ERROR: cep invalido ou nao encontrado!")
    elif choice == '2':
        try:
            Ip(clear, requests, cian, white, Enter)
        except:
            print("ERROR: ip invalido ou nao encontrado!")
    elif choice == '3':
        try:
            Cnpj(clear, requests, cian, white, Enter)
        except:
            print("ERROR: cnpj invalido ou nao encontrado!")
    elif choice == '4':
        try:
            Placa(clear, requests, cian, white, Enter)
        except:
            print("ERROR: placa invalido ou nao encontrado!")
    else:
        restart()

clear()
options()

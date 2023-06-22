def Ip(clear, requests, cia, ba, Enter):
    clear()
    ip = input(f'{cia}DIGITE O IP{ba}: ')
    data = requests.get(f'https://ipwhois.app/json/{ip}').json()
    clear()
    print(f'''
{cia}IP{ba}: {data["ip"]}
{cia}CONTINENTE{ba}: {data ["continent"]}
{cia}PAIS{ba}: {data ["country"]}
{cia}CAPITAL{ba}: {data ["country_capital"]}
{cia}CODIGO DE AREA{ba}: {data ["country_phone"]}
{cia}ESTADO{ba}: {data ["region"]}
{cia}LATITUDE{ba}: {data ["latitude"]}
{cia}LONGITUDEDE{ba}: {data ["longitude"]}
{cia}PROVEDOR{ba}: {data ["asn"]}
''')
    Enter()
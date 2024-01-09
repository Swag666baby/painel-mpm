def Ip(clear, requests, cian, white, restartCode):
    clear()
    ip = input(f'{cian}DIGITE O IP{white}: ')
    data = requests.get(f'https://ipwhois.app/json/{ip}').json()
    clear()
    print(f'''
{cian}IP{white}: {data["ip"]}
{cian}CONTINENTE{white}: {data ["continent"]}
{cian}PAIS{white}: {data ["country"]}
{cian}CAPITAL{white}: {data ["country_capital"]}
{cian}CODIGO DE AREA{white}: {data ["country_phone"]}
{cian}ESTADO{white}: {data ["region"]}
{cian}LATITUDE{white}: {data ["latitude"]}
{cian}LONGITUDEDE{white}: {data ["longitude"]}
{cian}PROVEDOR{white}: {data ["asn"]}
''')
    restartCode()

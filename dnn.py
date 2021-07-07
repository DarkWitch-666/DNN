import requests
import os
import time
from bs4 import BeautifulSoup as BS

# | v.1. | open-source | name: DNN |
RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

def get_html(url):
	return requests.get(url).text

def parse_ua(tutilka):
	soup = BS(tutilka, 'html.parser')
	for date in soup.findAll('td'):
		content = date.getText().split('  ')
		for g in content:
			if g == '':
				pass
			elif '\n' in g:
				g = g.replace("\n", "")
			else:
				print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)

os.system("clear")
print(f'''{BOLD}\033[35m
  mmmm          mmmm
 m"  "m        m"  "m
 #    #        #    #
 #    #        #    #
  #mm#          #mm#

       """""" 
   
{GREEN}1{CYAN} - Поиск по номеру телефона
{GREEN}2{CYAN} - Поиск Информации по IP
{GREEN}3{CYAN} - Прокси парсер
{GREEN}4{CYAN} - Тех поддержка
{GREEN}0{CYAN} - очистить терминал

{RED}[Автор: t.me/DarkWitch_666]\n[DNN-V1] (выход: ctrl + z)
''')

while True:
	shell = input(f'{CYAN}[{RED}*{CYAN}] Выберите пункт: {GREEN}')
	if shell == '1':
		phone = input(f'{CYAN}[{RED}*{CYAN}] Номер: +{GREEN}')
		try:
			response = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone)
			data = response.json()
			user_country = data[ 'country' ][ 'english' ]
			user_id = data[ 'country' ][ 'id' ]
			user_location = data[ 'country' ][ 'location' ]
			user_city = data[ 'capital' ][ 'english' ]
			user_lat = data[ 'capital' ][ 'latitude' ]
			user_log = data[ 'capital' ][ 'longitude' ]
			user_post = data[ 'capital' ][ 'post' ]
			user_oper = data[ '0' ][ 'oper' ]
			uty = requests.get("https://api.whatsapp.com/send?phone="+phone)
			if uty.status_code==200:
				utl2 = "https://api.whatsapp.com/send?phone="+phone
			else:
				utl2 = 'Not founded!'
			userr_all_info = f'{CYAN}[{RED}*{CYAN}] Country: {GREEN}{str(user_country)}\n{CYAN}[{RED}*{CYAN}] ID: {GREEN}{str(user_id)}\n{CYAN}[{RED}*{CYAN}] Location: {GREEN}{str(user_location)}\n{CYAN}[{RED}*{CYAN}] City: {GREEN}{str(user_city)}\n{CYAN}[{RED}*{CYAN}] Latitude: {GREEN}{str(user_lat)}\n{CYAN}[{RED}*{CYAN}] Longitude:{GREEN} {str(user_log)}\n{CYAN}[{RED}*{CYAN}] Index post:{GREEN} {str(user_post)}\n{CYAN}[{RED}*{CYAN}] Operator:{GREEN} {str(user_oper)}'
			num_name = []
			phone_ow = requests.get(f'https://phonebook.space/?number=%2B{phone}').text
			content = BS(phone_ow, 'html.parser').find('div', class_='results')
			for i in content.find_all('li'):
				num_name.append(i.text.strip())
			name = ', '.join(num_name)
			user_all_info = f"""
\033[35m-===[Основная информация]===-
{userr_all_info}
\033[35m-===[Ссылки]===-
{CYAN}[{RED}*{CYAN}] WhatsApp: {GREEN}{utl2}
\033[35m-===[Персональная информация]===-
{CYAN}[{RED}*{CYAN}] Вероятные имена: {GREEN}{name}
	"""
			print(user_all_info)
		except:
			print(f'{CYAN}[{RED}=<{CYAN}] произошла ошибка')
	elif shell == '2':
		query = input(f'{CYAN}[{RED}*{CYAN}] IP: {GREEN}')
		try:
			r = requests.get(f'http://ip-api.com/json/{query}').json()
			print(f'{CYAN}[{RED}*{CYAN}] Country:{GREEN} {r["country"]}\n{CYAN}[{RED}*{CYAN}] CountryCode:{GREEN} {r["countryCode"]}\n{CYAN}[{RED}*{CYAN}] Region:{GREEN} {r["region"]}\n{CYAN}[{RED}*{CYAN}] Region Name:{GREEN} {r["regionName"]}\n{CYAN}[{RED}*{CYAN}] City: {GREEN}{r["city"]}\n{CYAN}[{RED}*{CYAN}] Zip:{GREEN} {r["zip"]}\n{CYAN}[{RED}*{CYAN}] Latinude: {GREEN}{r["lat"]}\n{CYAN}[{RED}*{CYAN}] Longitude: {GREEN}{r["lon"]}\n{CYAN}[{RED}*{CYAN}] Timezone: {GREEN}{r["timezone"]}\n{CYAN}[{RED}*{CYAN}] ISP:{CYAN} {r["isp"]}\n{CYAN}[{RED}*{CYAN}] Org:{GREEN} {r["org"]}\n{CYAN}[{RED}*{CYAN}] As: {GREEN}{r["as"]} ')
		except:
			print(f'{CYAN}[{RED}-{CYAN}] Не найдено')
	elif shell == '3':
		res1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')
		print(f'{CYAN}[{RED}^_^{CYAN}] \nВаши прокси мисье:\n' + '\n'.join(res1.text.split('\r\n')))
	elif shell == '4':
		print('''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░█░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░██░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░▄▄███▄░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒░░░░░░░░░░░░▐██▌░░░░░░░▒▒▒▒▒▒▒▒
▒▒▒░░░░░░░░░░░░░░▀█░░░░░░░░░▒▒▒▒▒▒▒
▒▒░░░░░░░░░░░░░░▄███░░░░░░░░░▒▒▒▒▒▒
▒░░░░░░░░░░░░░░░████░░░░░░░░░░▒▒▒▒▒
▒░░░░▄░░░░░░░░░▐████░░░░░░░░░░▒▒▒▒▒
▒░░░░░▀▀▄░░░░▄█▀░███░░░░░░░░░░▒▒▒▒▒
▒░░░░░░░░▀▀█▀░░░░▐███░░░░░░░░░▒▒▒▒▒
▒▒░░░░░░░░░░▀▄▄▄▄████▌░░░░░░░▒▒▒▒▒▒
▒▒▒░░░░░░░░░██████████░░░░░░▒▒▒▒▒▒▒
▒▒▒▒░░░░░░░░░█████████░░░░░▒▒▒▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░▀██████░▀▄░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░▀████▄░▀▀▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▀██▄▒▒▒▀▄▄▄▄▄▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█▄▒▒▒▒███▄▀█
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀███▀▀
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▒

---------------------
Tg: DarkWitch_666
---------------------
Gmail: larrygreenberg007@gmail.com
---------------------
Number: +18319996553 (только звонки)
---------------------
''')
	elif shell == '0':
		os.system("python3 dnn.py")
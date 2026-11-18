# #скриптец для мониторинга выхода hyper os 4 на мою трубу ахах
from datetime import datetime
import winsound
import requests
import time
from bs4 import BeautifulSoup

def timeStamp ():   #логирование ластовой проверки
	file = open ('checkUpdate.txt', 'a')
	now = datetime.now ()
	string_format = now.strftime ('%Y-%m-%d %H:%M:%S')
	file.write (f"{string_format}\n")
	file.close () 

def notification():      #издает серию из 10ти звуков
	for i in range(1, 10):
		winsound.Beep(i * 100, 200)
	input ()

def getAllCells (url): #вырезает из html dom текстовые ячейки из таблицы
	response = requests.get (url)
	dom = BeautifulSoup (response.text, "html5lib")
	global_table_cells = dom.find ('tbody').find_all ('td')
	return global_table_cells

def checkUpdate (global_table_cells, old_version, isMonitoring): #сверяет данные ячеек с меня интересующими
	if global_table_cells[1].string == 'Not yet' and old_version.casefold () in global_table_cells[2].string.casefold ():
		print (f"Обновления НЕТ\n")
	else:
		print ("Обновление ПРИЛЕТЕЛО!!!")
		isMonitoring = False
		notification () 


url = 'https://xiaomifirmware.com/firmware/dash/#xf-global'
old_version = 'OS3.0.304.0.WPLMIXM' 
isMonitoring = True

while isMonitoring:
	global_table_cells = getAllCells (url) #чекаем 1й сайт
	checkUpdate (global_table_cells, old_version, isMonitoring) # чек на 1ом сайте урл
	timeStamp ()
	time.sleep (300)

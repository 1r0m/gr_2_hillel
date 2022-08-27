import requests
import pprint

def number():
	num = int(input("Вкажіть число до 100:"))

	while num <= 100:
		if num <= 100 :
			print("Повторіть введене число")
		if num < 0:
			print("Число менше 0 введіть число більше")
		elif num == 0:
			print("Число дорівнює 0")
			continue
	print("Ви ввели значення більше 100")

def URL():
	url = 'https://script.google.com/macros/s/AKfycbymoe4FLilr2JMNUshhMEYDqDlFqjGo06Y8e2IqQ-q-dNVDQjdS77Qz_QVIz4iRRIAa/exec'

	response = requests.get(url)
	data = response.json()
	pprint.pprint(data)

def len_list():
	text_message = input("Напишіть повідомлення менше за 150 символів:")
	text = text_message[:150]
	print(len(text))
	new_text = '...'
	result = text[:-3] + new_text
	print(result)
	
	with open(r"E:\\python.txt", 'w') as file:
		file.write(result)
		

	
	

if __name__ == '__main__':
	number()
	URL()
	len_list()
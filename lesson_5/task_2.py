import requests
import pprint

url = 'https://script.google.com/macros/s/AKfycbymoe4FLilr2JMNUshhMEYDqDlFqjGo06Y8e2IqQ-q-dNVDQjdS77Qz_QVIz4iRRIAa/exec'


def get_data_api_url(url):
    response = requests.get(url)
    data = response.json()
    return data


def check_number_in_range(number, low=0, hight=100):
    if number >= low and number <= hight:
        return True
    return False


def message_cater(string, lengs=150):
	message_text = input("")

	text = message_text[:lengs]
	lengs_text = len(message_text)


	if lengs_text > lengs:
		new_text = '...'
		result = message_text[:-3] + new_text
		print(result)
	else:
		print(message_text)


def write_file_in_document():
	with open(r"E:\\python.txt", 'w') as file:
		file.write(result)
		


if __name__ == '__main__':
	get_data_api_url(url=url)
	check_number_in_range()
	message_cater()
	write_file_in_document()

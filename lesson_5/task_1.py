import requests
import pprint

URL = 'https://script.google.com/macros/s/AKfycbymoe4FLilr2JMNUshhMEYDqDlFqjGo06Y8e2IqQ-q-dNVDQjdS77Qz_QVIz4iRRIAa/exec'

response = requests.get(URL)
data = response.json()
pprint.pprint(data)

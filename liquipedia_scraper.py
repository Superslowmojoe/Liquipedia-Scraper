from bs4 import BeautifulSoup
import requests

url = 'https://liquipedia.net/rocketleague/Rocket_League_Championship_Series/2021-22/Winter'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')


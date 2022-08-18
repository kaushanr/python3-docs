# API Project

#!pip install pyfiglet

import requests

url = 'https://raw.githubusercontent.com/kaushanr/python3-docs/main/docs/heading_art.py'
r = requests.get(url)
with open('/content/heading_art.py', 'w') as f:
    f.write(r.text)

from heading_art import heading

try: # contains error handling for pyfiglet installation
    print(heading('DAD JOKE 5000'))
except ModuleNotFoundError as err:
    print(err)
    print('Please install \'pyfiglet\' module to continue - >!pip install pyfiglet<')

category = input('Let me tell you a joke! Give me a topic : ')
print()
print('Disclaimer** Severe Cringe Alert!','\n')

url = 'https://icanhazdadjoke.com/search?'
response = requests.get(url,
                        headers = {'Accept':'application/json'},
                        params = {'term':category}
                        )

data = response.json()

if data['total_jokes']:

  from random import choice
  from termcolor import colored

  print(f'I\'ve got {data["total_jokes"]} jokes about {category}. Here\'s one : ')
  joke = choice(data['results'])['joke']
  result = colored(joke,color = 'red',attrs = ['bold'])
  print(result)
else:
  print(f'Sorry, I don\'t have any jokes about {category}!. Please try again.')

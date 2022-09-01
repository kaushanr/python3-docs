def my_load(file_name,url = 'https://raw.githubusercontent.com/kaushanr/python3-docs/main/docs/'):
  '''my_load(file_name,url = DefaultParameter)'''
  import requests
  url = url + file_name
  r = requests.get(url)
  with open(file_name, 'w') as f:
      f.write(r.text)
  return print(f'Loaded : {file_name}, to workspace.')

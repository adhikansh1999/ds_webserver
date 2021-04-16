import requests


url = 'https://gist.githubusercontent.com/sanketRmeshram/2e0c71add59402cc26f1a518e425e0a8/raw/54fa3eb1720a18ca9e8b89f3d2adc65316269d40/all_ip.txt'
r = requests.get(url, allow_redirects=True)


print(r.content)
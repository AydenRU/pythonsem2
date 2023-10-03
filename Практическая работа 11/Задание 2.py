import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

data = urllib.request.urlopen("https://quke.ru/shop/smartfony/apple?page-size=72").read().decode()
name =  r'(?:<a class="b-card2-v2__name" href=")(?:[^\"]+)(?:" title=")([^\"]+)'
cost = r'(?:<span class="b-card2-v2__price-val">)([^<]+)'

name_find = re.findall(name, data)
cost_find = re.findall(cost, data)
print(name_find, cost_find)

cost_phone = dict(map(lambda x, y: (x, int(y.replace(" ", ""))), name_find, cost_find))


f = open("catalog.csv", 'w')
for n, p in cost_phone.items():
    f.write(f'{n}: {p}\n')
    print(f'{n}: {p}\n')

name_count = 72
minimum = min(cost_phone.values())
maximum = max(cost_phone.values())
average = round(sum(cost_phone.values()) / name_count)

f.write(f'\nmin: {str(minimum)} \n')
print(f'\nmin: {str(minimum)} \n')
f.write(f'max: {str(maximum)} \n')
print(f'max: {str(maximum)} \n')

f.write(f'average: {str(average)} \n')
print(f'average: {str(average)} \n')
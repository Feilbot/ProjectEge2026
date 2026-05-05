# Библиотека для работы с сетями
from ipaddress import *

# Позволяет преобразовать текст в ip-адрес
ip = ip_address('172.16.128.0')

net = ip_network('172.16.128.0/255.255.192.0')

ip_bin = f'{int(ip):032b}'
print(ip_bin)
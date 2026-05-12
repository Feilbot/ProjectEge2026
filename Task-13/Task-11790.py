from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') >= ip[16:].count('0')

for x in range(0, 8):
    A = int('1' * x + '0' * (8 - x), 2)
    net = ip_network(f'152.65.245.132/255.255.{A}.0', False)
    if all(f(ip) for ip in net):
        print(A)
        break

for x in range(16, 25):
    net = ip_network(f'152.65.245.132/{x}', False)
    if all(f(ip) for ip in net):
        print(str(net.netmask).split('.')[2])
        break
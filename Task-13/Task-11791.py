from ipaddress import ip_network

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')

for x in range(16, 25):
    net = ip_network(f'246.51.128.202/{x}', False)
    if all(f(ip) for ip in net):
        print(str(net.netmask).split('.')[2])
        break
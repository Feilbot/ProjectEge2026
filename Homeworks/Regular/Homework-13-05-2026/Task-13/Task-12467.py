from ipaddress import ip_network, ip_address

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:].count('1') > 3

for A in range(0, 256):
    ip = ip_address(f'183.192.{A}.0')
    net = ip_network(f'{ip}/255.255.252.0', False)
    if all(f(ip) for ip in net):
        print(A)
        break
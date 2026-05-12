from ipaddress import ip_network, ip_address

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:24].count('0') > ip[24:].count('0')

ans = 0

for A in range(256):
    ip = ip_address(f'246.81.65.{A}')
    net = ip_network(f'{ip}/255.255.255.224', False)
    if ip in net.hosts() and all(f(ip) for ip in net.hosts()):
            ans += 1

print(ans)
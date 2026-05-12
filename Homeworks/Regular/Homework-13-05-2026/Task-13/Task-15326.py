from ipaddress import ip_network

net = ip_network('105.224.200.224/255.255.255.224', False)
ans = 0

for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 4 == 0:
        ans += 1

print(ans)
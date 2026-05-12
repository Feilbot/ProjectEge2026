from ipaddress import ip_address, ip_network

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')

ans = 0

for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net.hosts() and ip2 in net.hosts():
        ans = mask

print(ans)
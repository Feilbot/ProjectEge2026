from ipaddress import ip_network, ip_address

ip1 = ip_address('211.115.61.154')
ip2 = ip_address('211.115.59.137')

ans = 0

for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net.hosts() and ip2 in net.hosts():
        ans = max(int(str(net.netmask).split('.')[2]), ans)

print(ans)
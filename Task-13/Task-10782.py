from ipaddress import ip_address, ip_network

ip1 = ip_address('118.187.59.255')
ip2 = ip_address('118.187.65.115')

ans = 0

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net1.hosts() and ip2 in net2.hosts() and net1 != net2:
        ans = mask

print(ans)
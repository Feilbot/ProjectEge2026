from ipaddress import ip_address, ip_network

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

ans = []

for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if ip1 in net.hosts() and ip2 in net.hosts():
        ans.append(net.num_addresses)

print(min(ans))
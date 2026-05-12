from ipaddress import ip_network, ip_address

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net1.hosts() and ip2 in net2.hosts() and net1 != net2:
        print(str(net1.netmask).split('.')[2])
        break
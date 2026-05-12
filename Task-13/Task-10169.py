from ipaddress import ip_network, ip_address

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net1.hosts() and ip2 in net2.hosts() and net1 != net2:
        print(mask)
        break
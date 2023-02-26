from ipaddress import *
import sys

def check_ip_network_type(address):
    try:
        return 4 if type(ip_network(address)) is IPv4Network else 6
    except ValueError:
        return 10


def calc_wg_ip_range(allowed_networking: list, disallowed_networking: list) -> list:
    addr = []
    output = []
    for i in allowed_networking:
        count = 0
        for j in disallowed_networking:
            if j.subnet_of(i):
                for allowedip in i.address_exclude(j):
                    addr.append(allowedip)
                count += 1
        if count == 0:
            addr.append(i)
    for res in addr:
        for dis in disallowed_networking:
            if dis.subnet_of(res):
                addr.remove(res)
    for strings in addr:
        output.append(str(strings))
    return output


data = sys.argv[1:]
if len(data) == 0:
    print("Usage: [-a] AllowedIPs. comma to split the multiple ips. [-d] DisallowedIPs. comma to split\nExample: allow 0.0.0.0/0, 2001:db8::/32 and disallow 2001:db8:4001:103::/64, please use python3 wg.py -a 0.0.0.0,2001:db8::/32 -d 2001:db8:4001:103::/64")
    exit(1)
allow_ip_raw = data[data.index('-a') + 1].split(',')
disallow_ip_raw = data[data.index('-d') + 1].split(',')
allowed_ipv4 = []
allowed_ipv6 = []
disallowed_ipv4 = []
disallowed_ipv6 = []
for ipa in allow_ip_raw:
    if check_ip_network_type(ipa) == 4:
        allowed_ipv4.append(IPv4Network(ipa))
    elif check_ip_network_type(ipa) == 6:
        allowed_ipv6.append(IPv6Network(ipa))
for ipd in disallow_ip_raw:
    if check_ip_network_type(ipd) == 4:
        disallowed_ipv4.append(IPv4Network(ipd))
    elif check_ip_network_type(ipd) == 6:
        disallowed_ipv6.append(IPv6Network(ipd))
result = f"AllowedIPs = {', '.join(calc_wg_ip_range(allowed_ipv4, disallowed_ipv4) + calc_wg_ip_range(allowed_ipv6, disallowed_ipv6))}"
print(result)

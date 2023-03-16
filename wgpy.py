from ipaddress import *


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


allow_ip_raw = ["0.0.0.0/0","::0/0"]
disallow_ip_raw = ["10.0.0.0/8","fc00::/7"]
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
result = calc_wg_ip_range(allowed_ipv4, disallowed_ipv4) + calc_wg_ip_range(allowed_ipv6, disallowed_ipv6)
output = list(set(result))
output.sort(key=result.index)
print(f"AllowedIPs = {', '.join(output)}")

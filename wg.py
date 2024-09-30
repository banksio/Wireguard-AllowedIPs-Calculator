import argparse
import ipaddress
import typing


T = typing.TypeVar("T", list[ipaddress.IPv4Network], list[ipaddress.IPv6Network])


def check_ip_network_type(address: str):
    try:
        return 4 if type(ipaddress.ip_network(address)) is ipaddress.IPv4Network else 6
    except ValueError:
        return 10


def calc_wg_ip_range(
    allowed_networking: T,
    disallowed_networking: T,
) -> list:
    addr = []
    output: list[str] = []
    for i in allowed_networking:
        count = 0
        for j in disallowed_networking:
            if j.subnet_of(i):  # type: ignore
                for allowedip in i.address_exclude(j):  # type: ignore
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


def check_raw_ips(allow_ip_raw, disallow_ip_raw):
    allowed_ipv4: list[ipaddress.IPv4Network] = []
    allowed_ipv6: list[ipaddress.IPv6Network] = []
    disallowed_ipv4: list[ipaddress.IPv4Network] = []
    disallowed_ipv6: list[ipaddress.IPv6Network] = []
    for ipa in allow_ip_raw:
        if check_ip_network_type(ipa) == 4:
            allowed_ipv4.append(ipaddress.IPv4Network(ipa))
        elif check_ip_network_type(ipa) == 6:
            allowed_ipv6.append(ipaddress.IPv6Network(ipa))
    for ipd in disallow_ip_raw:
        if check_ip_network_type(ipd) == 4:
            disallowed_ipv4.append(ipaddress.IPv4Network(ipd))
        elif check_ip_network_type(ipd) == 6:
            disallowed_ipv6.append(ipaddress.IPv6Network(ipd))
    return allowed_ipv4, allowed_ipv6, disallowed_ipv4, disallowed_ipv6


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        required=True,
        type=str,
        metavar="AllowedIPs",
        help="allowed CIDR networks (comma-separated)",
    )
    parser.add_argument(
        "-d",
        required=True,
        type=str,
        metavar="DisallowedIPs",
        help="disallowed CIDR networks (comma-separated)",
    )

    args = parser.parse_args()

    allow_ip_raw: list[str] = args.a.split(",")
    disallow_ip_raw: list[str] = args.d.split(",")
    allowed_ipv4, allowed_ipv6, disallowed_ipv4, disallowed_ipv6 = check_raw_ips(
        allow_ip_raw, disallow_ip_raw
    )
    result = calc_wg_ip_range(allowed_ipv4, disallowed_ipv4) + calc_wg_ip_range(
        allowed_ipv6, disallowed_ipv6
    )
    output = list(set(result))
    output.sort(key=result.index)
    print(f"AllowedIPs = {', '.join(output)}")


if __name__ == "__main__":
    main()

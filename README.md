# WireGuard-AllowedIPs-Calculator
A simple WireGuard AllowedIPs calculator.

## Usage

```
wg.py [-h] -a AllowedIPs -d DisallowedIPs

options:
  -h, --help        show this help message and exit
  -a AllowedIPs     allowed CIDR networks (comma-separated)
  -d DisallowedIPs  disallowed CIDR networks (comma-separated)
```

For example:

```
$ python wg.py -a 0.0.0.0,2001:db8::/32 -d 2001:db8:4001:103::/64

AllowedIPs = 0.0.0.0/32, 2001:db8:8000::/33, 2001:db8::/34, 2001:db8:6000::/35, 2001:db8:5000::/36, 2001:db8:4800::/37, 2001:db8:4400::/38, 2001:db8:4200::/39, 2001:db8:4100::/40, 2001:db8:4080::/41, 2001:db8:4040::/42, 2001:db8:4020::/43, 2001:db8:4010::/44, 2001:db8:4008::/45, 2001:db8:4004::/46, 2001:db8:4002::/47, 2001:db8:4000::/48, 2001:db8:4001:8000::/49, 2001:db8:4001:4000::/50, 2001:db8:4001:2000::/51, 2001:db8:4001:1000::/52, 2001:db8:4001:800::/53, 2001:db8:4001:400::/54, 2001:db8:4001:200::/55, 2001:db8:4001::/56, 2001:db8:4001:180::/57, 2001:db8:4001:140::/58, 2001:db8:4001:120::/59, 2001:db8:4001:110::/60, 2001:db8:4001:108::/61, 2001:db8:4001:104::/62, 2001:db8:4001:100::/63, 2001:db8:4001:102::/64
```

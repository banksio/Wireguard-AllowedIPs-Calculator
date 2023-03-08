# Wireguard-AllowedIPs-Calculator
---

# Simple Wireguard AllowedIPs Calculator

## Usage:

## wg.py (Cli output)

`python3 wg.py -a 0.0.0.0,2001:db8::/32 -d 2001:db8:4001:103::/64`

[-a] AllowedIPs. comma to split the multiple ips.
[-d] DisallowedIPs. comma to split the multiple ips.

## wgpy.py

The same version but accept parameter in python script. you can modify it to your code.

```python
allow_ip_raw = ["0.0.0.0/0","::0/0"]
# Replace the allowed(routed) IP ranges with your IP.
disallow_ip_raw = ["10.0.0.0/8","fc00::/7"]
# Replace the disallowed(not routed) IP ranges with your IP.
```

Warning:THIS PROGRAM IS NO GUARANTEE! PLEASE USE IT AT YOUR OWN RISK. ILLEGAL USE IS STRICTLY PROHIBITED.

---
# 简单好用的Wireguard路由IP计算器

## 使用方法:

## wg.py (Cli输出)

`python3 wg.py -a 0.0.0.0,2001:db8::/32 -d 2001:db8:4001:103::/64`

[-a] 允许的IP段，使用逗号分割。
[-d] 不允许的IP段，使用逗号分割。

## wgpy.py

相同版本，但不通过Cli指定参数，可以修改后应用于其他代码。

```python
allow_ip_raw = ["0.0.0.0/0","::0/0"]
# 用允许的IP(路由的)IP段来替换上面的内容。
disallow_ip_raw = ["10.0.0.0/8","fc00::/7"]
# 用不允许的IP(直接路由不通过wg的IP段)IP段来替换上面的内容。
```

警告：本程序无任何保证, 请自行承担使用风险。严禁利用本程序进行非法活动。本程序作者不负任何责任。

# 簡単なWireguard AllowedIPs計算機

## 使用方法:

## wg.py (Cli出力)

`python3 wg.py -a 0.0.0.0,2001:db8::/32 -d 2001:db8:4001:103::/64`

[-a] アクセス許可のIP範囲指定，コンマで多IPを分割する。
[-d] アクセス禁止のIP範囲指定，コンマで多IPを分割する。

## wgpy.py

上記と同じだが、Cliでパラメータを取得しない。プログラム内で指定する。編集した後で他のコードでも利用可能。

```python
allow_ip_raw = ["0.0.0.0/0","::0/0"]
# アクセス許可のIP(ルートしたいIP)で替える。
disallow_ip_raw = ["10.0.0.0/8","fc00::/7"]
# アクセス禁止のIP(ルートしたくないIP)で替える。
```

ご注意ください：本プロジェクトは保証なし。自己責任。本プロジェクトを利用して違法犯罪行為をすることは固く禁じます。

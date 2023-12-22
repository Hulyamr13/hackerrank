import re

def validate_addresses(addresses):
    ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    for address in addresses:
        if ipv4_pattern.match(address):
            print('IPv4')
        elif ipv6_pattern.match(address):
            print('IPv6')
        else:
            print('Neither')

if __name__ == '__main__':
    address_count = int(input())
    addresses = [input() for _ in range(address_count)]
    validate_addresses(addresses)

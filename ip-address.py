#!/usr/bin/python3

import re

def test_ip_address(ip_address):
    regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    match = re.match(regex, ip_address)
    if match:
        print(f"{ip_address} is a valid IP address.")
    else:
        print(f"{ip_address} is not a valid IP address.")

# Test with some IP addresses
test_ip_address("192.168.0.1")
test_ip_address("10.0.0.255")
test_ip_address("172.16.254.1")
test_ip_address("256.0.0.1")  # Not a valid IP address
test_ip_address("192.168.0.1.2")  # Not a valid IP address


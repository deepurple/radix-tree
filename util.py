#!/usr/bin/env python
# coding: utf-8

def ip_to_bin(ip_str):
    return ''.join([bin(int(x))[2:].rjust(8, '0') for x in ip_str.split('.')])

def bin_to_ip(bin_str):
    return '.'.join([str(int(bin_str[0:8], 2)),
                     str(int(bin_str[8:16], 2)),
                     str(int(bin_str[16:24], 2)),
                     str(int(bin_str[24:32], 2))])

if __name__ == '__main__':
    ip_addr = '192.168.0.1'
    bin_str = ip_to_bin(ip_addr)
    ip_str = bin_to_ip(bin_str)
    print bin_str
    print ip_str
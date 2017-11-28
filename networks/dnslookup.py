# -*- coding:utf-8 -*-
# Find all of the ip by a hostname
from dns import resolver
from IPy import IP

def gethostbyname(host,nameservers):
    res = resolver.Resolver()
    res.nameservers = nameservers
    answers = res.query(host)
    ips = set()
    for rdata in answers:
        ips.add(rdata.address)
        #print (rdata.address)
    return ips

def gethostnamesSet():
    nameservers = ['114.114.114.114', '8.8.8.8', '101.226.4.6', '123.125.81.6', '101.226.4.6', '202.116.48.8']
    ips_new=set()
    with open('d://hostnames-in-VPN.TXT', 'r') as f:
        for domain in f.read().splitlines():
            ips_new.update(gethostbyname(domain, nameservers))
    return ips_new

def getVPNipsSet():
    vpn_ips = set()
    with open('d://ips-in-VPN.TXT', 'r') as f:
        for domain in f.read().splitlines():
            ip, mask = domain.split('/')
            ips = IP(IP(ip).make_net(mask))
            for x in ips:
                vpn_ips.add(x)
    return vpn_ips

def main():
    vpn_ips = getVPNipsSet()
    ips_new=gethostnamesSet()
    for ip_new in ips_new:
        print IP(ip_new) in vpn_ips,ip_new
    #print (ips - vpn_ips)

main()
from active_scan import port_scanning_active,directory_enumeration,service_discovery_active,subdomain_enumeration_active
from passive_scan import port_passive, pserv, wdg
from extra_tool import *
import socket


def active(domain,url):
    ip=socket.gethostbyname(domain)
    #Port Scan Result
    prt=port_scanning_active.Commonp_Scanner(ip) 

    #Directory Enum Result
    dir=directory_enumeration.direnum(url)
    # subd=subdomain_enumeration_active.brute_subd(url)
    # return 
    return ip+'\n'+prt+'\n'+dir

def passive(domain):
    pasport=port_passive.scanner(domain)
    passervdis=pserv.serv_pas(domain)
    wi=wdg.whois_inp(domain)
    dns=wdg.dns_info(domain)
    return 'Ports: \n'+pasport+'\nServices \n'+passervdis+'\nWhois \n'+wi+'\nDNS Details: \n'+dns

    






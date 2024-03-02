from active_scan import port_scanning_active,directory_enumeration,service_discovery_active,subdomain_enumeration_active
from passive_scan import port_passive, pserv, wdg
from extra_tool import *
import socket


def active(domain,url,port_num):
    ip=socket.gethostbyname(domain)
    
    #Port Scan Result
    res_prt=port_scanning_active.Commonp_Scanner(ip,port_num) 
    
    #Directory Enum
    dir_enum = directory_enumeration.direnum(url)

    #Subdomain Enum
    subd=subdomain_enumeration_active.brute_subd(url)

    #Service


    return ip+'\n'+res_prt+'\n'+dir_enum+'\n'+subd
# print(auto_port_scan('127.0.0.1'))




#Directory Enum Result
# dir=directory_enumeration.direnum(url)
# subd=subdomain_enumeration_active.brute_subd(url)

def passive(domain):
    pasport=port_passive.scanner(domain)
    passervdis=pserv.serv_pas(domain)
    wi=wdg.whois_inp(domain)
    dns=wdg.dns_info(domain)
    return 'Ports: \n'+pasport+'\nServices \n'+passervdis+'\nWhois \n'+wi+'\nDNS Details: \n'+dns

    






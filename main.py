from active_scan import port_scanning_active,directory_enumeration,service_discovery_active,subdomain_enumeration_active
from passive_scan import port_passive, wdg
from extra_tool import *
import socket


def active(domain,url,port_num):

    #IP Addr
    ip=socket.gethostbyname(domain)
    
    #Port Scan Result
    res_prt=port_scanning_active.Commonp_Scanner(ip,port_num) 
    
    #Directory Enum
    dir_enum = directory_enumeration.direnum(url)

    #Subdomain Enum
    subd=subdomain_enumeration_active.brute_subd(url)

    #Service Discovery
    serv_act=service_discovery_active.Scann(domain,port_num)

    return "IP Address of Domain: "+ip+'\n'+"Port Scan Result: \n"+res_prt+'\n'+'\n'+"Service Scan Result: \n"+serv_act+'\nCheck for vulnerabilities in the version.'+'\n'+"Confidential Directory lookup: \n"+dir_enum+'\n'+"Confidential Subdomain lookup: "+subd





def passive(domain):

    #Port Scan
    pasport=port_passive.scanner(domain)

    #Whois and DNS
    wi=wdg.whois_inp(domain)
    dns=wdg.dns_info(domain)

    return 'Ports: \n'+pasport+'\n\nWhois '+wi+'\n\nDNS Details: \n'+dns


    






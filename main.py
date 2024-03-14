from active_scan import port_scanning_active,directory_enumeration,service_discovery_active,subdomain_enumeration_active
from passive_scan import port_passive, wdg
import sqlite3
import socket
from urllib.parse import urlparse


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
    serv_act=service_discovery_active.Serv_Scanner(domain,port_num)

    return "IP Address of Domain: "+ip+'\n\n'+"Port Scan Result: \n"+res_prt+'\n'+'\n'+"Service Scan Result: \n"+serv_act+'\nCheck for vulnerabilities in the version.'+'\n'+"\nConfidential Directory lookup: \n"+dir_enum+'\n'+"\nConfidential Subdomain lookup: "+subd





def passive(domain):

    #Port Scan
    pasport=port_passive.scanner(domain)

    #Whois and DNS
    wi=wdg.whois_inp(domain)
    dns=wdg.dns_info(domain)

    return 'Ports: \n'+pasport+'\n\nWhois '+wi+'\n\nDNS Details: \n'+dns

def misc(username):
    data=f"C:\/Users\/{username}\/AppData\/Local\/Microsoft\/Edge\/User Data\/Default\/History"
    con=sqlite3.connect(data)
    cur=con.cursor()
    list_urls=cur.execute("SELECT * FROM urls ORDER BY ID DESC LIMIT 1")
    all_urls=list_urls.fetchall()
    list_elem=all_urls[0]
    elem=list_elem[1]
    last_url=''.join(elem)
    dom=urlparse(last_url).netloc
    return dom







    






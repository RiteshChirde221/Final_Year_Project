import whois
import dns.resolver
import requests
import socket

#Whois Lookup
def whois_inp(domain):
    w= whois.whois(domain)
    #Whois Data List
    wi_dl=["Whois Details: ","Domain: {}".format('  '.join(map(str,w.domain_name))),"Registrar: {}".format(w.registrar),
           "Name Servers: {}".format('  '.join(map(str,w.name_servers))),"Email: {}".format(w.email),"Oraganization: {}".format(w.organization), 
           "City: {}".format(w.city),"State: {}".format(w.state),"Country: {}".format(w.country)]
    return '\n'+' \n'.join(map(str,wi_dl))
# print(whois_inp('google.com'))

#DNS Lookup
def dns_info(domain):
    di_dl=[]
    try:
        for a in dns.resolver.resolve(domain,'A'):
            di_dl.append(a.to_text() )
    except None:
        di_dl.append('Not Found')      
    try:
        for ns in dns.resolver.resolve(domain,'NS'):
            di_dl.append(ns.to_text()) 
    except None:
        di_dl.append('Not Found')
    try:
        for mx in dns.resolver.resolve(domain,'MX'):
            di_dl.append(mx.to_text()) 
    except None:
        di_dl.append('Not Found')
    try:
        for txt in dns.resolver.resolve(domain,'TXT'):
            di_dl.append(txt.to_text()) 
    except None:
        di_dl.append('Not Found')
    
    return ' \n'.join(di_dl)

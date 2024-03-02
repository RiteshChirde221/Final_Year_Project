import whois
import dns.resolver
import requests
import socket

#Whois Lookup
def whois_inp(domain):
    try:
        w= whois.whois(domain)
    #Whois Data List
        if w.name_servers or w.email ==None:
           wi_dl=['Error']
        else:
            wi_dl=["Name Servers: {}".format('  '.join(map(str,w.name_servers))),"Email: {}".format(w.email)]
    except OSError:
        wi_dl=['Connection Error']
    return '\n'+' \n'.join(map(str,wi_dl))
# print(whois_inp('google.com'))

#DNS Lookup
def dns_info(domain):
    di_dl=[]
    try:
        for a in dns.resolver.resolve(domain,'A'):
            di_dl.append(a.to_text() )
    except BaseException:
        di_dl.append('A record Connection Error or Not Found')      
    try:
        for ns in dns.resolver.resolve(domain,'NS'):
            di_dl.append(ns.to_text()) 
    except BaseException:
        di_dl.append('NS Record Connection Error or Not Found')
    try:
        for mx in dns.resolver.resolve(domain,'MX'):
            di_dl.append(f'Check the mail that should not be accessible or visible to normal users in the above list and disable it \n {mx.to_text()}') 
    except BaseException:
        di_dl.append('MX record Connection Error or Not Found')
    
    return ' \n'.join(di_dl)

# print(dns_info('google.com'))

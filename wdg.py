import whois
import dns.resolver
import requests
import socket

#Whois Lookup
def whois_inp(domain):
    w= whois.whois(domain)
    #Whois Data List
    wi_dl=[w.domain_name, w.registrar, w.updated_date,
           w.creation_date, w.expiration_date,
           w.name_servers, w.email, w.organization, 
           w.city, w.state, w.country]
    for i in wi_dl:
        if i is None:
            pass
        else:
            print(i)

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
    
    for i in di_dl:
        print(i)

#GeoLocation Lookup
def geoloc(domain):
    r=requests.get("https://geolocation-db.com/json/"+socket.gethostbyname(domain))
    res=r.json()
    # Geo location data list
    gl_dl=[res['country_name'], res['latitude'], res['longitude'],
           res['city'], res['state'], res['postal']]
    return print('{}\n{}\n{}\n{}\n{}\n{}'.format(*gl_dl))  #print the lisst as string
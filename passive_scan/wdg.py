import whois
import dns.resolver


wi_dl=[]
#Whois Lookup
def whois_inp(domain):
    w= whois.whois(domain)
        #Whois Data List
    wi_dl=["Discovered Name Servers from whois are : \n{}".format('\n'.join(map(str,w.name_servers)))+' ,\ncheck for forbidden nameservers and hide them.',"Emails discovered are: \n{}".format(w.email)+' ,\ncheck for forbidden email and hide them.']
    return '\n'+' \n'.join(map(str,wi_dl))


#DNS Lookup
def dns_info(domain):
    di_dl=[]
    try:
        di_dl.append("A Record of domain is: ")
        for a in dns.resolver.resolve(domain,'A'):
            di_dl.append(a.to_text() )
    except BaseException:
        di_dl.append('A record Connection Error or Not Found')      
    try:
        di_dl.append("Nameserver found in ns record are :")
        for ns in dns.resolver.resolve(domain,'NS'):
            di_dl.append(ns.to_text()) 
    except BaseException:
        di_dl.append('NS Record Connection Error or Not Found')
    try:
        for mx in dns.resolver.resolve(domain,'MX'):
            di_dl.append(f'Check the mail that should not be accessible or visible to normal users in the above list and disable it:\n{mx.to_text()}') 
    except BaseException:
        di_dl.append('MX record Connection Error or Not Found')
    
    return '\n'.join(di_dl)




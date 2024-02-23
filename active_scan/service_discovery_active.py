from nmap import *
import socket

prt=['21','22','23','80','443','8080','53','3306']
def Scanner(ip,port):
    scanner=PortScanner()
    res=scanner.scan(ip,port)
    scan_res=res['scan'][ip]['tcp']
    serv_state=scan_res[int(port)]['state']
    serv_name=scan_res[int(port)]['name']
    serv_product=scan_res[int(port)]['product']
    serv_version=scan_res[int(port)]['version']
    serv_extrainfo=scan_res[int(port)]['extrainfo']
    serv_cpe=scan_res[int(port)]['cpe']
    return 'Port: '+port+'State: '+serv_state,'Name: '+serv_name+'Product: '+serv_product+'Version: '+serv_version+'ExtraInfo: '+serv_extrainfo+'CPE: '+serv_cpe

def Scann(domain):
    res=[]
    ip=socket.gethostbyname(domain)
    for port in prt:
        res.append(Scanner(ip,port))
        return ' \n'.join(res)

 
from nmap import *
import socket


res=[]
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
    return serv_cpe[7:]

def Scann(domain,prt):
    ip=socket.gethostbyname(domain)
    for port in prt:
        res.append(Scanner(ip,port))
        return ''.join(map(str,res))


 
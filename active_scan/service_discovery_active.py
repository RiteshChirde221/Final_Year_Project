from nmap import *
import socket

res=[]
def Serv_Scanner(domain,prt):
    var=[]
    ip=socket.gethostbyname(domain)
    for port in prt.split(','):
        var.append(Service_Scan(ip,port))
    return ''.join(var)
    

def Service_Scan(ip,port):
    scanner=PortScanner()
    res=scanner.scan(ip,port)
    serv=res['scan'][ip]['tcp'][int(port)]
    state=serv.get('state')
    name=serv.get('name')
    product=serv.get('product')
    version=serv.get('version')
    extrainfo=serv.get('extrainfo')
    cpe=serv.get('cpe')
    return 'State: '+state+'\nName: '+name+'\nProduct: '+product+'\nVersion: '+version+'\nExtrainfo: '+extrainfo+'\nCPE: '+cpe+'\n\n'

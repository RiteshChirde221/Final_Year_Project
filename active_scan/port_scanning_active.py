from nmap import *

prt=['21','22','23','80','443','8080','53','3306']

def Scanner(ip,port):
    scanner=PortScanner()
    res=scanner.scan(ip,port)
    scan_res=res['scan'][ip]['tcp']
    port_res=scan_res[int(port)]['state']
    return "\nPort {port}: {port_res} ".format( port=port, port_res=port_res)

def Commonp_Scanner(ip):
    res=[]
    for port in prt:
        res.append(Scanner(str(ip),port))
    result=""
    return result.join(res)

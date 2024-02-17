from nmap import *

ip='127.0.0.1'
prt=['90','8080']
sr_prt=89
er_prt=91
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
    return print('Port: ',port,'State: ',serv_state,'Name: ',serv_name,
            'Product: ',serv_product,'Version: ',serv_version,
            'ExtraInfo: ',serv_extrainfo,'CPE: ',serv_cpe)

def Specified_Scanner():
    for port in prt:
        Scanner(ip,port)

def Range_Scanner():
    for port in range(sr_prt,er_prt+1):
        Scanner(ip,port.__str__())
if __name__=="__main__":
    # Specified_Scanner()
    Range_Scanner()
 
from nmap import *

ip='127.0.0.1'
prt=['90','8080']
sr_prt=89
er_prt=91
def Scanner(ip,port):
    scanner=PortScanner()
    res=scanner.scan(ip,port)
    scan_res=res['scan'][ip]['tcp']
    return print(scan_res)

def Specified_Scanner():
    for port in prt:
        Scanner(ip,port)

def Range_Scanner():
    for port in range(sr_prt,er_prt+1):
        Scanner(ip,port.__str__())
if __name__=="__main__":
    # Specified_Scanner()
    Range_Scanner()
 
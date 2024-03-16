from nmap import *

def Scanner(ip,port):
    scanner=PortScanner()
    res=scanner.scan(ip,port,arguments='-sS') #using stealth mode to reduce requests
    scan_res=res['scan'][ip]['tcp']
    port_res=scan_res[int(port)]['state']
    return port_res


def Commonp_Scanner(ip,prt):
    res=[]
    for port in prt.split(','):
        var=Scanner(ip,port)
        if var=='filtered':
            res.append(f'Port {port} is filtered')
        elif var=='closed':
            res.append(f'Port {port} is closed request is not blocked by firewall, Configuring the firewall is nedded')
        elif var=='open':
            res.append(f'Port {port} is open request not blocked by firewall, Configuring the firewall is nedded.')
    return ' \n '.join(res)


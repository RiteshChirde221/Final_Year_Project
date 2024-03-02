from pybinaryedge import BinaryEdge
import socket

s=set()
portls=[]

def scanner(domain):
    try:
        be = BinaryEdge('d0ee1761-6bb8-4b67-b463-51f9cc9a743e')
# Iterate over the first page of IPs having specific ssh configuration
        ip=socket.gethostbyname(domain)
        search = f'ip:{ip}'
        results = be.host_search(search)
        
        for ports in results['events']:
            s.add(ports['target']['port'])
        for port in s:
            p=f"Port {port} is open not filtered by firewall.\n Check with active scan to confirm"
            portls.append(p)
    except OSError:
        portls.append('Connection Error')
    return '\n '.join(portls)
# print(scanner('prmceam.ac.in'))

#API connection
#api=d0ee1761-6bb8-4b67-b463-51f9cc9a743e

#API search limited to 250 
#and pages to 1000
# print(scanner('prmceam.ac.in'))

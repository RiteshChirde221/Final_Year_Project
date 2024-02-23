from pybinaryedge import BinaryEdge
import socket

def scanner(domain):
    be = BinaryEdge('d0ee1761-6bb8-4b67-b463-51f9cc9a743e')
# Iterate over the first page of IPs having specific ssh configuration
    ip=socket.gethostbyname(domain)
    search = f'ip:{ip}'
    results = be.host_search(search)
    s=set()
    portls=[]
    for ports in results['events']:
        s.add(ports['target']['port'])
# print(s)
    for port in s:
        portls.append(port)
    return 'Port open are :'+', '.join(map(str,portls))

#API connection
#api=d0ee1761-6bb8-4b67-b463-51f9cc9a743e

#API search limited to 250 
#and pages to 1000

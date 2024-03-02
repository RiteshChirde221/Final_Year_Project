from whatweb import *
def serv_pas(domain):
    try:
        res=whatweb(domain)
        out=res.split()
    except OSError:
        out=['Connection Error']
    
    return '\n'.join(out)

# print(serv_pas('google.com'))









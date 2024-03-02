import requests
restricted_subdomains = [
    'admin',
    'controlpanel',
    'internal',
    'dev',
    'staging',
    'uat',
    'test',
    'preview',
    'beta'
]

def brute_subd(url):
    sub_list=[]
    try:
        for ssd in restricted_subdomains:
            if url[0:5]=='https':
                if url[8:12]=='www.':
                    res_url=url[:12]+ssd+'.'+url[12:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nAlive: {res_url} should not be accesible by customer")
                else:
                    res_url=url[:8]+ssd+'.'+url[8:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nAlive: {res_url} should not be accesible by customer")
            elif url[0:5]=='http:':
                if url[7:11]=='www.':
                    res_url=url[:11]+ssd+'.'+url[11:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nAlive: {res_url} should not be accesible by customer")
                else:
                    res_url=url[:7]+ssd+'.'+url[7:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nAlive: {res_url} should not be accesible by customer")
            else:
                pass
    except OSError:
        sub_list.append(f"\nCheck Internet or URL")
    return ''.join(sub_list)

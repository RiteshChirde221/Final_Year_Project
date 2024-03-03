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
    'beta',
    'testphp'
]


def brute_subd(url):
    sub_list=[]
    for ssd in restricted_subdomains:
        try:
            if url[0:5]=='https':
                if url[8:12]=='www.':
                    res_url=url[:12]+ssd+'.'+url[12:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nSubdomain: {res_url} should not accessible remotely to normal user for security measures \n")
                else:
                    res_url=url[:8]+ssd+'.'+url[8:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nSubdomain: {res_url} should not accessible remotely to normal user for security measures \n")
            elif url[0:5]=='http:':
                if url[7:11]=='www.':
                    res_url=url[:11]+ssd+'.'+url[11:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nSubdomain: {res_url} should not accessible remotely to normal user for security measures \n")
                else:
                    res_url=url[:7]+ssd+'.'+url[7:]
                    res=requests.get(res_url)
                    sub_list.append(f"\nSubdomain: {res_url} should not accessible remotely to normal user for security measures \n")
                # if res.status_code==404:/
            else:
                pass
        except OSError:
                pass
    return ''.join(sub_list)
                    


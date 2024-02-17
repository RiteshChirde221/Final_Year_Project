import requests
def brute_subd(url):
    subwl='subd.txt'
    with open(subwl,'r') as file:
        sub_wl=[line.rstrip() for line in file]
        for ssd in sub_wl:
            try:
                if url[0:5]=='https':
                    if url[8:12]=='www.':
                        res_url=url[:12]+ssd+'.'+url[12:]
                        res=requests.get(res_url)
                        print(f"Alive: {res_url}")
                    else:
                        res_url=url[:8]+ssd+'.'+url[8:]
                        res=requests.get(res_url)
                        print(f"Alive: {res_url}")
                elif url[0:5]=='http:':
                    if url[7:11]=='www.':
                        res_url=url[:11]+ssd+'.'+url[11:]
                        res=requests.get(res_url)
                        print(f"Alive: {res_url}")
                    else:
                        res_url=url[:7]+ssd+'.'+url[7:]
                        res=requests.get(res_url)
                        print(f"Alive: {res_url}")
                # if res.status_code==404:/
                else:
                    print("Not Found: {}".format(res_url)) 
            except OSError:
                print("Check Internet or URL ",ssd)
                    
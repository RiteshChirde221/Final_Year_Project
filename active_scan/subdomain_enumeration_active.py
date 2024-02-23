import requests
def brute_subd(url):
    subwl='D:\/Final_year_Project\/Project_source\/active_scan\/subd.txt'
    with open(subwl,'r') as file:
        sub_list=[]
        sub_str=""
        sub_wl=[line.rstrip() for line in file]
        for ssd in sub_wl:
            try:
                if url[0:5]=='https':
                    if url[8:12]=='www.':
                        res_url=url[:12]+ssd+'.'+url[12:]
                        res=requests.get(res_url)
                        sub_list.append(f"\nAlive: {res_url}")
                    else:
                        res_url=url[:8]+ssd+'.'+url[8:]
                        res=requests.get(res_url)
                        sub_list.append(f"\nAlive: {res_url}")
                elif url[0:5]=='http:':
                    if url[7:11]=='www.':
                        res_url=url[:11]+ssd+'.'+url[11:]
                        res=requests.get(res_url)
                        sub_list.append(f"\nAlive: {res_url}")
                    else:
                        res_url=url[:7]+ssd+'.'+url[7:]
                        res=requests.get(res_url)
                        sub_list.append(f"\nAlive: {res_url}")
                # if res.status_code==404:/
                else:
                    sub_list.append("\nNot Found: {}".format(res_url)) 
            except OSError:
                sub_list.append("\nCheck Internet or URL ",ssd)
    return sub_str.join(sub_list)
                    
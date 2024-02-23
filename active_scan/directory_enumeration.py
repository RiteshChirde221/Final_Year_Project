import requests

def direnum(url):
    #Location of worlist file
    wordlist="D:\/Final_year_Project\/Project_source\/active_scan\/dir.txt" #get from user
    with open(wordlist,'r') as file:
        dir_wl=[line.rstrip() for line in file]
    dir_list=[]
    dir_str=""
    for i in dir_wl:
        dirsearch=url+i
        res=requests.get(dirsearch)
        if res.status_code==404:
            dir_list.append('\nNot Found: {}'.format(dirsearch))
        else:
            dir_list.append('\nAlive url:{}'.format(dirsearch))
    return dir_str.join(dir_list)

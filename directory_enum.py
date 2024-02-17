import requests

def direnum(url):
    #Location of worlist file
    wordlist='' #get from user
    with open(wordlist,'r') as file:
        dir_wl=[line.rstrip() for line in file]
    for i in dir_wl:
        dirsearch=url+i
        res=requests.get(dirsearch)
        if res.status_code==404:
            print('Not Found: {}'.format(dirsearch))
        else:
            print('Alive URLS:', dirsearch)


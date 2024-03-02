import requests


restricted_paths = [
    'admin',
    'admin_panel',
    'userinfo.php',
    'control_panel',
    'config',
    'config_files',
    'logs',
    'cart.php',
    'error_logs',
    'temp',
]



def direnum(url):
    dir_list=[]
    for i in restricted_paths:
        dirsearch=url+i
        res=requests.get(dirsearch)
        if res.status_code==404:
            pass
        else:
            dir_list.append(f'{i} should not be accessible remotely:{dirsearch} \n')
    return ''.join(dir_list)

# print(direnum('http://127.0.0.1:90'))
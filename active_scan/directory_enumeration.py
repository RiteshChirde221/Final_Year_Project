import requests


restricted_paths = [
    '/admin',
    '/admin_panel',
    '/control_panel',
    '/config',
    '/config_files',
    '/logs',
    '/error_logs',
    '/temp',
    '/temp_files',
    '/cache',
    '/cache_files',
    '/backup',
    '/backup_files',
    '/uploads',
    '/uploads_files',
    '/source',
    '/source_code',
    '/restricted_pages',
    '/restricted_functionalities'
]



def direnum(url):
    dir_list=[]
    for i in restricted_paths:
        dirsearch=url+i
        res=requests.get(dirsearch)
        if res.status_code==404:
            pass
        else:
            dir_list.append(f'{i} should not be accessible remotely:{dirsearch}')
    return ''.join(dir_list)

# print(direnum('http://127.0.0.1:90'))
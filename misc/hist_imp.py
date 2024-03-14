import sqlite3

data="C:\/Users\/rohan\/AppData\/Local\/Microsoft\/Edge\/User Data\/Default\/History"
con=sqlite3.connect(data)
cur=con.cursor()
list_urls=cur.execute("SELECT url FROM urls")
all_urls=list_urls.fetchall()

print(all_urls)

def each_url(all_urls):
    for elem in all_urls:
        last_url=''.join(elem)
    return last_url




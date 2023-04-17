import requests
from multiprocessing import Pool

urls=['https://bigmir.net']

def crowling(t):
    global urls
    indi='href="'

    i=0
    if indi in t:
        while i!=-1:
            i=t.find(indi)
            j=t[i+len(indi):].find('"')+i+len(indi)
            url=t[i+len(indi):j]
            if url[0]=='h' and url not in urls:
                urls.append(url)
            t=t[j:]
        urls.pop(len(urls)-1)

crowling(requests.get(urls[0]).text)

def proces(i):
    global urls
    try:
        t=requests.get(urls[i])
        crowling(t.text)
    except:
        pass

for i in range(1):
    with Pool(100) as p:
        p.map(proces, range(i*100, i*100+99))


for i in urls:
    print(i)
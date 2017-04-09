import requests,asyncio,random,os,time
from concurrent.futures import ThreadPoolExecutor,as_completed

def get_4m_pix(query="snow sun",ed_ch='true'):
    urls=[]
    key="4428699-9ef870c32a232e1906813ae46"
    url="https://pixabay.com/api/"
    dic={}
    dic['key']=key
    dic['q']=query
    dic['editors_choice']=ed_ch

    res = requests.get(url,params=dic)
    if res.status_code!=200:
        print("BOY U FUCKED UP!!!!")
        return []

    ans = res.json()
    imgs = ans['hits']
    for d in imgs:
        urls.append(d['webformatURL'].replace('_640','_960'))

    return urls

def get_img(url):
    res = requests.get(url)
    
    if res.status_code!=200:
        print("Problem with :",url)
        return
    data = res.content
    a,b=random.randint(1,9999),random.randint(10000,99999)
    name = str(a)+str(b)+'.jpg'
    f=open('c:/downs/'+name,"wb")
    f.write(data)
    f.close()
    return url

def download_thread(urls):
    x=time.clock()
    try:
        os.mkdir('c:/downs')
    except:
        pass
    #for u in urls:
        #q.put_nowait(u)

    pool = ThreadPoolExecutor(max_workers=10)
    fs=[]
    for u in range(len(urls)):
        f=pool.submit(get_img,urls[u])
        f.i=u
        fs.append(f)
        
    for f in as_completed(fs):
        print(f.i)
    print(time.clock()-x)

def main():
    q=input("search query:")
    urls = get_4m_pix(query=q)
    download_thread(urls)
main()

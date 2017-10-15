import requests,asyncio,random,os,time
from https import get_http_obj 

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

async def get_img(url,u):
    try:
        data = await get_http_obj(url)
        print("OK",u)
    except:
        print("problem",u)
    
    
    a,b=random.randint(1,9999),random.randint(10000,99999)
    name = str(a)+str(b)+'.jpg'
    f=open('c:/downs/'+name,"wb")
    f.write(data)
    f.close()

async def download(urls,loop):
    try:
        os.mkdir('c:/downs')
    except:
        pass

    fs = []
    for u in range(len(urls)):
        f=asyncio.ensure_future(get_img(urls[u],u))
        fs.append(f)

    print("assigned")
    await asyncio.wait(fs)
    print("Done")

loop = asyncio.get_event_loop()
q="cat" #input("search query:")
urls = get_4m_pix(query=q)
x=time.clock()
loop.run_until_complete(download(urls,loop))
print(time.clock()-x)











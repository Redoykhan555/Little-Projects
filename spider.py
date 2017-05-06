from lxml import html
import requests,os,time
from concurrent.futures import ThreadPoolExecutor as tpe,wait

site = "https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/"
dest = "h:/The Fountian (2004)/resource"

page = requests.get(site)
tree = html.fromstring(page.content)

p='//*[@id="non_code_bar"]'
root = tree.xpath(p)[0]

def allLinks(root):
    ans = []
    for e in root.getchildren():
        if e.tag=='a':
            ans+=[e.attrib['href']]
        else:
            ans += allLinks(e)
    return set(ans)

def download(url):
    path = os.path.join(dest,url.split('/')[-1])
    data = requests.get(url)
    with open(path,'wb') as f:
        f.write(data.content)

links = allLinks(root)
pool = tpe(max_workers=4)
t=time.clock()
fs = []
for li in links:
    print("downloading ...", li)
    f = pool.submit(download,site+li)
    fs.append(f)
    print("Done")

wait(fs)
print(time.clock()-t)

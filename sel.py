from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time

driver = web.Chrome()
d=driver

def do(func,*args):
    while True:
        try:
            func(*args)
            return
        except:
            pass

def qlogin(driver,user="",passwd=""):
    d.get("https://www.quora.com")
    email = "redoykhan555@gmail.com"
    passwd = [122, 120, 99, 118, 98, 110, 109, 108, 107, 106, 37, 53]

    passwd = ''.join([chr(i) for i in passwd])
    form = driver.find_element_by_class_name('regular_login')
    username = form.find_element_by_name('email')
    username.send_keys(user)

    password = form.find_element_by_name('password')
    password.send_keys(passwd)

    password.send_keys(Keys.RETURN)


def ysearch(d,query):
    d.get("https://www.youtube.com/")
    s = d.find_element_by_name("search_query")
    s.send_keys(query)
    s.send_keys(Keys.RETURN)

    contr = d.find_element_by_id("content").find_element_by_id("page-manager")
    cont = contr.find_element_by_id("container").find_element_by_id("primary")
    vid = cont.find_element_by_id("video-title")
    url = vid.get_attribute("href")
    d.get(url)


def book(q):
    q = q.split()
    q='+'.join(q)
    u = f"http://93.174.95.27/search.php"
    param = f"?req={q}&open=0&res=25&view=simple&phrase=1&column=def"

    d.get(u+param)
    tbody = d.find_element_by_xpath("/html/body/table[3]/tbody")
    books = tbody.find_elements_by_tag_name("tr")[1:]
    for i in range(len(books)):
        b=books[i]
        print(i+1)
        ats = b.find_elements_by_tag_name("td")
        prop = ["ID","Authors(s)","Title","Publisher","Year","pages",
                "Language","Size","Extension"]
        for j in range(len(prop)):
            print(prop[j],ats[j].text)

        print()

    ind = int(input("Choose an index: "))
    link = books[ind-1].find_elements_by_tag_name("td")[9]
    url=link.find_element_by_tag_name("a").get_attribute("href")
    d.get(url)
    e=d.find_element_by_xpath('/html/body/table/tbody/tr/td[3]/a[1]')
    print("Downloading....")
    d.get(e.get_attribute("href"))


book("functional programming")


























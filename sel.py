from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time

driver = web.Chrome()
d=driver

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

def do(func,*args):
    while True:
        try:
            func(*args)
            return
        except:
            pass

do(ysearch,d,"viva la vida")
